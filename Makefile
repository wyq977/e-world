# --- Configuration ---
BIB_FILE  = e-world.bib
MD_SOURCE = pubs.md
CSL_STYLE = csl/american-physics-society.csl
CSS_FILE  = style.css
OUT_FILE  = index.html

# --- Flags ---
# --standalone: Creates full HTML page
# --citeproc:   Process citations
# --css:        Link your custom width styles
PANDOC_FLAGS = --standalone --citeproc --metadata title="Publications" --css=$(CSS_FILE)

# --- Rules ---

all: $(OUT_FILE)

# Build the HTML
$(OUT_FILE): $(MD_SOURCE) $(BIB_FILE) $(CSL_STYLE) $(CSS_FILE)
	@echo "Building $(OUT_FILE) using $(CSL_STYLE)..."
	pandoc $(MD_SOURCE) -o $(OUT_FILE) \
		--bibliography=$(BIB_FILE) \
		--csl=$(CSL_STYLE) \
		$(PANDOC_FLAGS)
	@echo "Done."

# Switch style easily: make style CSL=csl/nature.csl
style:
	@make $(OUT_FILE) CSL_STYLE=$(CSL)

clean:
	rm -f $(OUT_FILE)

.PHONY: all clean style