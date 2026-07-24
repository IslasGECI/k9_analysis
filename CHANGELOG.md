# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.6.2] - 2026-07-24

### Fixed

- Update functions `get_maya_effort_distance()` and `get_maya_effort_time` to new pandas value extraction.

## [0.6.0] - 2023-02-20

### Added

- `write-total-time-and-distance-maya` CLI command that returns JSON summary output for Maya time and distance data via

### Fixed

- Column naming inconsistencies in effort summary output

## [0.5.3] - 2023-02-20

### Fixed

- Critical NA handling bug in effort and distance calculations

## [0.5.2] - 2023-02-20

### Fixed
- Data validation for missing values in duration fields

## [0.5.1] - 2023-02-10

### Added
- Create an effort and distance summary using `make_summary_of_effort_and_distance()`

## [0.5.0] - 2023-02-10

### Added
- `write-total-time-and-distance`CLI command to write a summary of time and distance from a given period.

## [0.4.5] - 2023-02-02

### Added

- `write-summary-of-marked-nests` CLI command for generating nest summaries by year

## [0.4.4] - 2023-02-01

## [0.4.3] - 2023-02-01

## [0.4.2] - 2023-01-31

## [0.4.1] - 2023-01-31

[Unreleased]: https://github.com/IslasGECI/k9_analysis/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/IslasGECI/k9_analysis/compare/v0.5.3...v0.6.0
[0.5.3]: https://github.com/IslasGECI/k9_analysis/compare/v0.5.2...v0.5.3
[0.5.2]: https://github.com/IslasGECI/k9_analysis/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/IslasGECI/k9_analysis/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/IslasGECI/k9_analysis/compare/v0.4.5...v0.5.0
[0.4.5]: https://github.com/IslasGECI/k9_analysis/compare/v0.4.4...v0.4.5
[0.4.4]: https://github.com/IslasGECI/k9_analysis/compare/v0.4.3...v0.4.4
[0.4.3]: https://github.com/IslasGECI/k9_analysis/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/IslasGECI/k9_analysis/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/IslasGECI/k9_analysis/releases/tag/v0.4.1
