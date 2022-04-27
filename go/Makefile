.PHONY: test todo

check: test todo

test:
	@go clean -testcache
	@go test ./...

todo:
	@rgrep -n --include "*.go" --include "*.md" --include "*.sh" "TODO" --exclude "release-checklist.md" || true
	@rgrep -n --include "*.go" "// REF" || true

cover:
	@go test --coverprofile=cover.out ./...
	@go tool cover -func=cover.out | tail -n1 | tr -s "\t"
	@go tool cover -html=cover.out -o cover.html
	@rm -f cover.out
