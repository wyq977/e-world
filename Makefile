# --- Configuration ---
BIB_FILE  = e-world.bib
MD_SOURCE = e-world.md
CSL_STYLE = csl/custom.csl
CSS_FILE  = style.css
OUT_FILE  = index.html

# --- Flags ---
# --citeproc: Process the [@citations]
# --metadata suppress-bibliography=true: Prevents printing the list again at the bottom
FLAGS = --standalone --citeproc --css=$(CSS_FILE)

# --- Rules ---

all: $(OUT_FILE)

$(OUT_FILE): $(MD_SOURCE) $(BIB_FILE) $(CSL_STYLE) $(CSS_FILE)
	pandoc $(MD_SOURCE) -o $(OUT_FILE) \
		--bibliography=$(BIB_FILE) \
		--csl=$(CSL_STYLE) \
		$(FLAGS)

# Regenerate the public list from wiki/sources frontmatter, then the HTML
list:
	python3 scripts/build_list.py
	$(MAKE) $(OUT_FILE)

# Human step: move a reviewed staging folder into the source layer
approve:
	@test -n "$(KEY)" || (echo "usage: make approve KEY=<citekey>"; exit 1)
	@test -d inbox/$(KEY) || (echo "no inbox/$(KEY)"; exit 1)
	@test ! -e raw/$(KEY) || (echo "raw/$(KEY) already exists"; exit 1)
	@grep -q "{$(KEY)," $(BIB_FILE) || echo "warning: $(KEY) not in $(BIB_FILE)"
	mv inbox/$(KEY) raw/$(KEY)
	@echo "approved: raw/$(KEY)"

clean:
	rm -f $(OUT_FILE)

.PHONY: all clean list approve
