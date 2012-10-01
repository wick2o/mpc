<?php

# Include Libraries
include("webbot_libs\LIB_http.php");
include("webbot_libs\LIB_parse.php");
include("webbot_libs\LIB_download_images.php");
$download_path = "C:\\downloads\\torrentz\\autoload\\";
$max = 10;
$last_page = "false";

for ( $counter = 1; $counter <= $max; $counter += 1) {
	$artist_ref="http://coda.fm/albums/just_added?page=" . $counter;
	$artist_return_array = http_get_withheader($artist_ref,$artist_ref);
    
	if ( strpos($artist_return_array['FILE'], "<h4>Added a few days ago</h4>") === false ) 
	{
		if ( strpos($artist_return_array['FILE'], "<h4>Added yesterday</h4>") === false )
		{
			$artist_data = parse_array($artist_return_array['FILE'], "<h4>Added today</h4>" ,"<div class='link' id='paginator'>");
		}
		else
		{
			$artist_data = parse_array($artist_return_array['FILE'], "<h4>Added today</h4>" ,"<h4>Added yesterday</h4>");
			$last_page = "true";
		}
	}
		
	else
	{
		
			$artist_data = parse_array($artist_return_array['FILE'], "<h4>Added today</h4>" ,"<h4>Added a few days ago</h4>");
			$last_page = "true";
	
			
	}

	if ( $artist_data == null ) { echo "Nothing for today"; exit; }
	
	$artist_links = parse_array($artist_data[0], "<a href='/albums" ,">"); 

	foreach ($artist_links as $art_link) {
		$album_ref = "http://www.coda.fm" . return_between($art_link, "<a href='", "'>", EXCL);
		$tor_return_array = http_get_withheader($album_ref,$album_ref);
		$tor_link = return_between($tor_return_array['FILE'], "<a class='link' href='/albums/", "'", EXCL);

		$myfile = download_binary_file("http://www.coda.fm/albums/" . $tor_link, "http://www.coda.fm");
        $myfile_name = return_between($tor_link,"file=", ".torrent", EXCL);
		echo $myfile_name . "\n";
		
		$fp = fopen($download_path . $myfile_name . ".torrent", "w");
        fputs($fp, $myfile);
        fclose($fp);
	}
	if ( "$last_page" == "true" ) { exit; }
}
?>