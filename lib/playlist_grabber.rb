require 'dotenv'
Dotenv.load
require 'yt'
require 'pry'

class PlaylistGrabber
  # def initialize
  #   Yt.configuration.api_key = ENV['YT_KEY']
  # end

  def grab_playlist(id)
    Yt.configuration.api_key = ENV['YT_KEY']
    playlist = Yt::Playlist.new(id: id)
    # binding.pry
    playlist.playlist_items.map do |video|
      video.video_id
    end
  end
end