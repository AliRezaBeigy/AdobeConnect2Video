import os
import argparse
import untangle
import subprocess
from .utilities import execute_ffmpeg, isMethod, isString, Struct

def extractMetadata(data_path):

    print("[+] Extract Metadata...")

    index_stream = untangle.parse(data_path + '/indexstream.xml')

    audio_streams = []
    video_streams = []

    for message in index_stream.root.Message:
        if isMethod(message, "playEvent") and isString(message, "streamAdded"):
            stream = Struct()
            stream.name = message.Array.Object.streamName.cdata.lstrip('/')
            stream.start_time = int(message.Array.Object.startTime.cdata)

            if 'screenshare' in stream.name:
                video_streams.append(stream)
            elif 'cameraVoip' in stream.name:
                audio_streams.append(stream)
        if isMethod(message, "playEvent") and isString(message, "streamRemoved"):
            stream = next(filter(lambda stream: stream.name == message.Array.Object.streamName.cdata.lstrip('/'), audio_streams + video_streams), None)
            if stream is not None:
                stream.end_time = int(message.Object.time.cdata)

    return (audio_streams, video_streams)

def generateAudio(data_path, output_path, audio_streams):
    
    print("[+] Generate Audio...")

    audio_output_file = os.path.join(output_path, 'audio.mp3')
    audio_commands = list(map(lambda audio_stream: f'-itsoffset {audio_stream.start_time}ms -i {os.path.join(data_path, audio_stream.name + ".flv")}', audio_streams))
    execute_ffmpeg(f'{" ".join(audio_commands)} -filter_complex "amix=inputs={len(audio_commands)}:duration=longest [aout]" -map [aout] -async 1 -r 5 -c:a libmp3lame {audio_output_file}')

    return audio_output_file

def generateVideo(data_path, output_path, video_streams, audio_path, resolution):
    time = 0
    final_videos = []
    inputs = [f"-i {audio_path}"]
    for video_stream in video_streams:
        no_video_duration = video_stream.start_time - time
        if no_video_duration > 0:
            no_video_path = os.path.join(os.path.realpath(__file__), '..', 'no_video.jpg')
            output_file = os.path.join(output_path, video_stream.name + "_blank.mp4")
            final_videos.append(output_file)
            inputs.append(f'-loop 1 -t {no_video_duration}ms -i {no_video_path}')
        filename = f'{os.path.join(data_path, video_stream.name)}.flv'
        final_videos.append(filename)
        duration = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
        inputs.append(f'-t {video_stream.end_time - video_stream.start_time}ms -i {os.path.join(data_path, video_stream.name)}.flv')
        time = video_stream.start_time + (float(duration) * 1000)

    output_file = os.path.join(output_path, "video.mp4")
    video_maps_1 = map(lambda i: f"[{i[0] + 1}:v]scale={resolution},setpts=PTS-STARTPTS[v{i[0]}];", enumerate(final_videos))
    video_maps_2 = map(lambda i: f"[v{i[0]}]", enumerate(final_videos))
    execute_ffmpeg(f'{" ".join(inputs)} -filter_complex "{"".join(video_maps_1)}{"".join(video_maps_2)}concat=n={len(final_videos)}:v=1:a=0:unsafe=1[v]" -map [v] -map "0:a" -r 5 -c:a libopus -af "highpass=300, lowpass=4000" -c:v libx265 -b:a 96k {output_file}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--id", type=str, required=True, help="the name of directory data is available"
    )
    parser.add_argument(
        "-d", "--data-path", type=str, required=False, help="the path extracted data must be available as directory"
    )
    parser.add_argument(
        "-o", "--output-path", type=str, required=False, help="the output path that generated data saved"
    )
    parser.add_argument(
        "-r", "--resolution", type=str, required=False, help="the resolution of output video", default='1920:1880'
    )
    # TODO repair mode -- rerender the screen share to fix duration issue
    args = parser.parse_args()
    
    video_id = args.id

    cwd = os.getcwd()
    data_path = os.path.join(args.data_path, video_id) if args.data_path is not None else os.path.join(cwd, 'data', video_id)
    output_path = args.output_path if args.output_path is not None else os.path.join(cwd, 'output')

    if not os.path.exists(output_path):
        os.mkdir(output_path)
        output_path = os.path.join(output_path, video_id)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
    else:
        output_path = os.path.join(output_path, video_id)
        if not os.path.exists(output_path):
            os.mkdir(output_path)

    (audio_streams, video_streams) = extractMetadata(data_path)
    audio_path = generateAudio(data_path, output_path, audio_streams)
    generateVideo(data_path, output_path, video_streams, audio_path, args.resolution)

    print("[+] Done!")

