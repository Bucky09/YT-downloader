from pytube import YouTube
import os

def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def download_video(url, output_path=".", resolution="highest"):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the video stream based on the selected resolution
        if resolution == "highest":
            video_stream = yt.streams.get_highest_resolution()
        else:
            video_stream = yt.streams.filter(res=resolution).first()

        # Download the video without prompting for output directory
        video_title = sanitize_filename(yt.title)
        video_stream.download(output_path, filename=f"{video_title}.mp4", filename_prefix='')

        print(f"\nDownload completed: {video_title}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    video_url = input("Enter the YouTube video URL: ")

    # Validate the URL for both regular and Shorts URLs
    if not (video_url.startswith("https://www.youtube.com/watch?v=") or video_url.startswith("https://www.youtube.com/shorts/")):
        print("Invalid YouTube video URL. Please enter a valid URL.")
        return

    # Prompt the user to choose video quality
    print("\nSelect video quality:")
    print("1. Highest Resolution")
    print("2. 720p")
    print("3. 360p")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        resolution = "highest"
    elif choice == "2":
        resolution = "720p"
    elif choice == "3":
        resolution = "360p"
    else:
        print("Invalid choice. Defaulting to highest resolution.")
        resolution = "highest"

    # Specify the output directory as the root directory
    output_directory = "."

    # Download the video
    download_video(video_url, output_directory, resolution)

if __name__ == "__main__":
    main()
