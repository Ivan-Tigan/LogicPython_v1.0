from yattag import Doc
from prooftohtml import *
import pyscreenshot as ImageGrab
from random import randint
import json
import webbrowser

from selenium import webdriver

import pdfkit
import win32com.client

import click

@click.command()
@click.argument('name')

def main(name):
    click.echo("{}".format(name))

    output_pdf_folder_location = 'C:/Users/User/........./pdf/'
    output_html_folder_location = 'C:/Users/User/........./html/'

    doc, tag, text = Doc().tagtext()
    proofName = name
    proofFile = 'proof\\' + proofName + '.proof'
    outputHTML = 'html\\' + proofName + '.html'
    outputImage= 'img\\' + proofName + '.png'
    outputPDF = proofName+'.pdf'

    with tag('html'):
            with tag('head'):
                doc.asis('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
                with tag('style'):
                    doc.asis('''
@media print {
  @page { margin: 0; }
  body { margin: 1.6cm; }
}                    
@media print {
  body {-webkit-print-color-adjust: exact;}
  }
.logicline {
  display: flex !important;
  /* margin-top: -0.5% !important; */
}
* {
  /* font-family: monospace; */
  font-size: 1.em;
  letter-spacing: 0px;
  line-height: 19px;
  font-stretch: extra-condensed;
}

.prf table { border-collapse: collapse; border: 2px black; table-layout: fixed;}
.prf tr { display: block; float: left; padding-right: 10px;}
.prf th, .prf td { display: block; text-align: left;}

table{
  border-collapse:collapse;
  border: 2px black;
  padding: 0px;
}

td{
  padding-right:10px;
  padding: 0px;
  margin:0px;
}
tr{

  padding: 0px;
  margin:0px;
  display: flex;
}


.vl{
  position: relative;
  }
.vl:after {
  content:"";
  background: black;
  position: absolute;
  left: 0;
  top: 0%;
  bottom: 0%;
  width: 1px;
  padding:0px;
  margin:0px;


  }


.tl{
  position: relative;
  }
   
.tl:after {
  content:"";
  background: black;
  position: absolute;
  top: 10%;
  right: 0px;
  left: -3px;
  height: 1px;
  padding:0px;
  margin:0px;


  }
  
  .tvl{
  position: relative;
  }
   
  .tvl:after {
  content:"";
  background: black;
  position: absolute;
  left: 0;
  top: 10%;
  bottom: 0%;
  width: 1px;
  padding:0px;
  margin:0px;


  }



  .bl{
    position: relative;
    }
     
  .bl:after {
    content:"";
    background: black;
    position: absolute;
    bottom: 10%;
    left: 0;
    right: -0px;
    left: -3px;
    height: 1px;
    padding:0px;
    margin:0px;
  
  
    }
  
.bvl{
  position: relative;
  }
   
  .bvl:after {
  content:"";
  background: black;
  position: absolute;
  left: 0;
  top:  0%;
  bottom: 10%;
  width: 1px;
  padding:0px;
  margin:0px;
  }
''')
            with tag('body'):
                makeProof(doc, tag, text, proofFile)

    makeHTML(doc, outputHTML)


    if __name__ == '__main__':
        from time import sleep
        sleep(0.05)
        # grab fullscreen
        im = ImageGrab.grab()
        height = len(open(proofFile,"r", encoding='utf-8').readlines())
        width = len(max(open(proofFile,"r", encoding='utf-8').readlines(), key=len))
        print(width)
        im = im.crop(box=(0,150,width*13.333,125+height*33))

        # save image file
        im.save(outputImage)

        #pdf and html files
        #comment this out if you do not want the functionality
        import win32com.shell.shell as shell
        commands = 'chrome --headless --disable-gpu --print-to-pdf=' + output_pdf_folder_location + outputPDF + ' file:///' + output_html_folder_location + proofName+'.html'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
        sleep(2)
        webbrowser.open('pdf\\'+outputPDF)
        #############
        
if __name__ == "__main__":
    main()

