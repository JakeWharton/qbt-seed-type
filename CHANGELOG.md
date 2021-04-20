# Changelog

## [Unreleased]


## [1.1.1] - 2021-04-20

Fixed

- Support torrents with different download locations that point to the same file.

  For example, a torrent with `a.txt` whose location is `/downloads/a` should be marked as a cross-seed of a torrent with `a/a.txt` whose location is `/downloads`.


## [1.1.0] - 2021-03-08

Changed

- Default cron now runs every 5 minutes rather than every hour.


## [1.0.0] - 2021-02-23

Initial release


[Unreleased]: https://github.com/JakeWharton/qbt-seed-type/compare/1.1.1...HEAD
[1.1.1]: https://github.com/JakeWharton/qbt-seed-type/releases/tag/1.1.1
[1.1.0]: https://github.com/JakeWharton/qbt-seed-type/releases/tag/1.1.0
[1.0.0]: https://github.com/JakeWharton/qbt-seed-type/releases/tag/1.0.0
