require "minitest/autorun"
require './lib/playlist_grabber'

class PlaylistGrabberTest < Minitest::Test
  def test_grabs_playlist_and_returns_list
    grabber = PlaylistGrabber.new
    videos = grabber.grab_playlist('')
    assert videos.size == 2
  end
end