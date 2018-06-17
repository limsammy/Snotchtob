require 'dotenv'
Dotenv.load
require 'yt'
require 'pry'
require 'faraday'

class PlaylistGrabber
  def initialize
    Yt.configuration.api_key = ENV['YT_KEY']
    @conn = Faraday.new(url: 'https://https://lolyoutube.com/download') do |faraday|
      faraday.adapter Faraday.default_adapter
    end
  end

  def grab_playlist(id)
    playlist = Yt::Playlist.new(id: id)
    videos = []
    playlist.playlist_items.each do |video|
      video_item = {}
      video_item[:id] = video.video_id
      video_item[:title] = video.title
      videos << video_item
    end
    videos
  end

  def save_playlist(playlist_id)
    playlist = grab_playlist(playlist_id)
    playlist.each do |video|
      download_page = get_json("/mp4/#{video[:id]}/" + DateTime.now.to_time.to_i.to_s)
      binding.pry
    end
  end

  private
    attr_reader :conn

    def get_json(url)
      begin
        response = conn.get(url)
        JSON.parse(response.body, symbolize_names: true)
      rescue
        return { err: "{connection error}" }
      end
    end
end