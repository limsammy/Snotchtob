require 'yt'
require 'dotenv'

class PlaylistGrabber
  def setup
    Yt.configuration.api_key = ENV['api_key']
  end

  def self.grab_playlist(id)
    setup
    playlist = Yt::PlaylistItem.new(id: 'PLjW_GNR5Ir0GWEP_ove')
    playlist
  end
end