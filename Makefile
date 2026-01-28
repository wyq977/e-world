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

clean:
	rm -f $(OUT_FILE)

.PHONY: all clean
