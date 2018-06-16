require 'yt'
require 'dotenv-rails'
require 'pry'

class PlaylistGrabber
  # def initialize
  #   Yt.configuration.api_key = ENV['YT_KEY']
  # end

  def grab_playlist(id)
    Yt.configuration.api_key = ENV['YT_KEY']
    playlist = Yt::PlaylistItem.new(id: 'PLjW_GNR5Ir0GWEP_ove')
    binding.pry
    playlist.playlist_items
  end
end