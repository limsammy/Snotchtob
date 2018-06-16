require 'test_helper'

class PlaylistGrabberTest < Minitest::Test
  def grabs_playlist_and_returns_list
    videos = PlaylistGrabber.grab_playlist('')
    assert videos == 2
  end
end