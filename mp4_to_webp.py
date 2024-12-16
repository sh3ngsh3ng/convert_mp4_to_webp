import subprocess

def convert_mp4_to_webp(input_file, output_file, fps=15, scale_width=640, quality=60):
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vf", f"fps={fps},scale={scale_width}:-1:flags=lanczos",
        "-c:v", "libwebp",
        "-quality", str(quality),
        "-loop", "0",
        output_file
    ]
    subprocess.run(command, check=True)
    print(f"Conversion complete! Saved to {output_file}")

# Example usage
convert_mp4_to_webp("1223.mp4", "output.webp")


# ffmpeg -i input.mp4 -vf "fps=15,scale=640:-1:flags=lanczos" -c:v libwebp -quality 75 -loop 0 output.webp