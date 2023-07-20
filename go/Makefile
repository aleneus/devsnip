.PHONY: test todo

check: test fixme

test:
	@go clean -testcache
	@go test ./...

fixme:
	@rgrep -n "TODO now" \
		--include "*.go" \
		--include "*.md" \
		--include "*.sh" \
		--exclude "release-checklist.md" \
		|| true

	@rgrep -n "// REF" \
		--include "*.go" \
		--include "*.sh" \
		|| true

cover:
	@go test --coverprofile=cover.out ./...
	@go tool cover -func=cover.out | tail -n1 | tr -s "\t"
	@go tool cover -html=cover.out -o cover.html
	@rm -f cover.out
