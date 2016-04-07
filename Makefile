MathTestFonts.zip: *.ttx *.py OFL.txt
	rm -f *.otf
	python generate-fonts.py
	ttx *.ttx
	zip -v $@ *.otf

clean:
	rm -f *.otf

distclean: clean
	rm -f *.zip
