require 'yt'
require 'dotenv'

class PlaylistGrabber
  def initialize
    Yt.configure do |config|
      config.api_key = ENV['api_key']
    end
  end

  def grab_playlist(id)
    playlist = Yt::PlaylistItem.new(id: 'PLjW_GNR5Ir0GWEP_ove')
    binding.pry
    playlist.playlist_items
  end
end