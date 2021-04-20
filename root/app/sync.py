#!/usr/bin/python3 -u

import os
from qbittorrentapi import Client

DEBUG = os.environ['DEBUG'] == 'true'

SOLO_TAG = os.environ['QBT_SOLO_TAG']
CROSS_TAG = os.environ['QBT_CROSS_TAG']
HOST = os.environ['QBT_HOST']
USER = os.environ['QBT_USER']
PASS = os.environ['QBT_PASS']

client = Client(host=HOST, username=USER, password=PASS)

if DEBUG:
	print('Creating file mapping counts...')

# Count the number of torrents which reference each file path.
file_to_count = dict()
for torrent in client.torrents.info():
	for file in torrent.files:
		file_path = torrent.save_path + file.name
		file_to_count[file_path] = file_to_count.get(file.name, 0) + 1

for torrent in client.torrents.info():
	if DEBUG:
		print('---', torrent.name, '---')
		print('Tags:', torrent.tags)

	is_cross = False
	for file in torrent.files:
		file_path = torrent.save_path + file.name

		if file.priority == 0:
			if DEBUG:
				print(file_path, "Ignored (priority == 0)")
			continue  # This file is not set to download. Ignore.
		if file.progress < 1:
			if DEBUG:
				print(file_path, "Ignored (progress < 1)")
			continue  # This file is not completed and may not have been linked. Ignore.

		torrent_reference_count = file_to_count[file_path]
		file_cross_seeded = torrent_reference_count > 1
		if DEBUG:
			print(file_path, torrent_reference_count, file_cross_seeded)
		if file_cross_seeded:
			is_cross = True
			break

	if DEBUG:
		print('Cross-seed?', is_cross)

	torrent_tags = torrent.tags.split(', ')
	if is_cross:
		if SOLO_TAG in torrent_tags:
			print('Clearing', SOLO_TAG, torrent.name)
			torrent.removeTags(SOLO_TAG)
		if CROSS_TAG not in torrent_tags:
			print('Tagging', CROSS_TAG, torrent.name)
			torrent.addTags(CROSS_TAG)
	else:
		if CROSS_TAG in torrent_tags:
			print('Clearing', CROSS_TAG, torrent.name)
			torrent.removeTags(CROSS_TAG)
		if SOLO_TAG not in torrent_tags:
			print('Tagging', SOLO_TAG, torrent.name)
			torrent.addTags(SOLO_TAG)
