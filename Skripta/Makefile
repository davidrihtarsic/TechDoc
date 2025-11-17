pdfs:
	@for ff in $(file); do \
		num=$$(echo $$ff | sed 's/_.*$$//'); \
		section=$$(echo $$num | sed 's/\..*$$//g'); \
		subsect=$$(echo $$num | sed 's/.*\.//g'); \
		[[ $$subsect -gt 0 ]] && subsect=$$((subsect-1)) || section=$$((section-1)); \
		sed -i "1i \ " $$ff; \
		sed -i "1i \\\\\setcounter{section}{$$section}\\\\\setcounter{subsection}{$$subsect}" $$ff; \
		pandoc2notebook -f $$ff; \
		sed -i "1,2d" $$ff; \
		done;

TITLE="Osnove 3D modeliranja in tehniškega risanja za učitelje tehnike in tehnologije"

# trenutno je nastavljeno, da iz direktorija vzamemo le dokumente, ki so namenjeni:
# - teoriji: [0-9]*T_*.md
#   če bi želeli vse datoteke je niz: [0-9]*.md

book:
	@echo "Compailing all chapters into book... $(TITLE)."
	@cat $$(ls --color=never -v [0-9]*T_*.md) > ./pdf/Modeliranje_in_tehniska_dokumentacija.md && echo ".. Done."
	@file_name=$$(echo $(TITLE) | sed 's/\ /_/g'); \
	pandoc ./pdf/Modeliranje_in_tehniska_dokumentacija.md --to latex -o ./pdf/Modeliranje_in_tehniska_dokumentacija.pdf \
		--from markdown \
		--template skripta.tex \
		-V lang=sl \
		-M title=$(TITLE) \
		-M subtitle="Modularni učni priročnik za bodoče učitelje tehnike in tehnologije. Začenja se z razumevanjem 3D modeliranja kot temelja tehniške predstavitve. Sledi sistematičen prehod v tehniško risanje in uporabo standardov. Združuje teorijo, prakso in pedagoški kontekst." \
		-M author:"dr. David Rihtaršič" \
		-M date:"$(date '+%Y-%B')" \
		--syntax-highlighting=idiomatic \
		-M listings=True \
		-M listings-no-page-break=True \
		-M codeBlockCaptions=True \
		-M listingTitle="Primer" \
		-M lstPrefix="prim." \
		-M figureTitle="Slika" \
		-M figPrefix=sl. \
		-M eqnPrefix=en. \
		-M lol=False \
		-V table-use-row-colors \
		-V urlcolor=violet \
		-V caption-justification=centering \
		--number-sections \
		-F pandoc-crossref \
		--citeproc \
		--bibliography="./bibtex.bib" \
		-V documentclass=book \
		-V book \
		--toc \
		--toc-depth=2 \
		-M titlepage;
	@rm ./pdf/Modeliranje_in_tehniska_dokumentacija.md

clean:
	@mv -f *.pdf ./pdf/

file := $(shell find ./ -type f -name "[0-9]*T_*.md"|sed 's/\.\///g'|sort)
all: pdfs book clean
