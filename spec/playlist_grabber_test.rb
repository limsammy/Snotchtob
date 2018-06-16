require "minitest/autorun"
require './lib/playlist_grabber'

class PlaylistGrabberTest < Minitest::Test
  def test_grabs_playlist_and_returns_list
    grabber = PlaylistGrabber.new
    videos = grabber.grab_playlist('PLcKFH-qaX7yigdFDf6WplLkFaMLSp9jeH')
    assert videos.size == 2
  end
end