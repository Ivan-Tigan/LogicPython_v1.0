# LogicPython_v1.0
This is a command line tool that can be used to format logic proofs in the style used in the University of Birmingham, which also closely resemples the Fitch style. <br>
There are two main files: <br>
prooftohtml.py can be used to generate the html skeleton for the structure of the proof. (the required css is in the other file) <br>
logicBuilder.py is the actual tool that can convert a file from the proof folder, which a .proof extension to a png and/or pdf, and/or html. The .png files are stored in the img folder automatically, whereas for the pdf and html files, currently, due to some technological difficulties and limitations, an absolute path must be given in the variables 'output_pdf_folder_location' and 'output_html_folder_location'. The system for creating the .png files, again due to some technological limitations/difficulties currently relies on taking a screenshot of the html file open in a browser (happens automatically), which means that results may differ depending on the browser, how large the window of the browser is, how zoomed in the contents of the browser are, etc. (Scalings for these things can be configured inside the code) (The .png system scales automatically for different sized proofs, although the scaling factor could be messed around with, too). <br>
There are examples of how to write the proofs in the 'proof' folder, and example output files in the 'png', 'pdf', and 'html' folders. <br>
I mainly made this tool so that I can submit my homework digitally instead of by handwriting, while still perfectly sticking to the style from the lectures and not shifting it to a style that has a tool for it, but is quite ultimatelly quite different.<br>

##Example

The following is an example (proof2b.proof):<br>
```
1. ∀x[P(x)→(Q(x)∨x=b)] ; Premise ; {1}<br>
2. { Q(b) ; Hypothesis ; {2}<br>
3. |{ P(a) ; Hypothesis ; {3}<br>
4. || P(a)→(Q(a)∨a=b) ; ∀-elimination1 ; {1}<br>
5. || Q(a)∨a=b ; →-elimination3,4 ; {1, 3}<br>
6. ||{ Q(a) ; Hypothesis ; {6}<br>
7. ||} Q(a) ; Restate6 ; {6}<br>
8. ||{ a=b ; Hypothesis ; {8}<br>
9. ||| а=а ; =-introduction ; {}<br>
10.||| b=a ; =-elimination8,9 ; {8}<br>
11.||| Q(b) ; Restate2 ; {2}<br>
12.||} Q(a) ; =-elimination10,11 ; {2,8}<br>
13.|} Q(a) ; ∨-elimination5,6,7,8,12 ; {1, 2, 3}<br>
14.| P(a)→Q(a) ; →-introduction3,13 ; {1, 2}<br>
15.} ∀x[P(x)→Q(x)] ; ∀-introduction14 ; {1, 2}<br>
16.Q(b)→∀x[P(x)→Q(x)] ; →-introduction2,15 ; {1} <br>
```
![Example Proof2b](img/proof2b.png?raw=true "Example .png output for a .proof input:")
