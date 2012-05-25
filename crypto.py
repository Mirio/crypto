#                                    LICENSE BSD 2 CLAUSE                                       #
#                   Copyright 2012 Mirio. All rights reserved.                                  #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        #


import gtk
import gtk.glade
import hashlib

def on_main_delete_event(widget, data=None):
	gtk.main_quit()
	return False

def converti_md5(widget, data=None):
	entra = testo_input.get_text()
	md = hashlib.md5()
	md.update(entra)
	uscita = output.set_text(md.hexdigest())
	
def converti_sha(widget, data=None):
	entra = testo_input.get_text()
	sh = hashlib.sha512()
	sh.update(entra)
	uscita = output.set_text(sh.hexdigest())
	
def converti_bin(widget, data=None):
	entra = testo_input.get_text()
	generabin = ''.join(format(ord(x), '8b') for x in entra)
	uscita = output.set_text(generabin)

def converti_text(widget, data=None):
	try:
		entra = testo_input.get_text()
		generachar = entra.split(' ')
		generachar_final = ''
		for x in generachar:
			generachar_encode = unichr(int(x, 2))
			generachar_final += generachar_encode
		uscita = output.set_text(generachar_final)
	except ValueError:
		bin_err_main.show()
		
def binerr_bottone(widget, data=None):
	bin_err_main.hide()

segnali = {
	'on_main_delete_event': on_main_delete_event ,
	'on_conv_md5_clicked': converti_md5 ,
	'on_conv_sha_clicked': converti_sha ,
	'on_conv_bin_clicked': converti_bin ,
	'on_conv_text_clicked': converti_text ,
	'on_binerr_bottone_clicked': binerr_bottone 
}

gladeFile = gtk.glade.XML(fname='crypto.glade')
gladeFile.signal_autoconnect(segnali)

wg = gladeFile.get_widget
output = wg('output')
testo_input = wg('testo_input')
Main = wg('main')
bin_err_main = wg('binerr_main')

Main.show()
gtk.main()
