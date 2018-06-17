require_relative 'playlist_grabber'

puts "Please enter a youtube playlist ID:"
id = gets.chomp

grabber = PlaylistGrabber.new
grabber.save_playlist(id)