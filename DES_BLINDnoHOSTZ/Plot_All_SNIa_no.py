#Make a pdf file containing plots of all the SNIa
#Can be adjusted to do it for other types

from astropy.io import ascii
import matplotlib.pyplot as plt

SNIa_list = ascii.read('SNIa_List.dat')

import matplotlib.backends.backend_pdf
import random

out_pdf = r'SNIa_Plots_noZ.pdf' #adjust for other types

pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
i = 0
figs = plt.figure()
while i<834: #adjust for other types
    plot_num = 321
    fig = plt.figure(figsize=(10, 8))
    for x in range(6):
        plt.rcParams.update({'font.size': 7.5})
        plt.subplot(plot_num)
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=0.5)
        rdr = ascii.get_reader(Reader=ascii.Basic)
        rdr.header.splitter.delimiter = ' '
        rdr.data.splitter.delimiter = ' '
        rdr.header.start_line = 12
        rdr.data.start_line = 13
        rdr.data.end_line = None
        t = rdr.read(SNIa_list['SNIa List'][i]) #adjust for other types
        MJD = t['MJD']
        FLT = t['FLT']
        FIELD = t['FIELD']
        FLUXCAL = t['FLUXCAL']
        FLUXCALERR = t['FLUXCALERR']
        plt.errorbar(MJD[FLT=='g'], FLUXCAL[FLT=='g'], FLUXCALERR[FLT=='g'], capsize = 4, label='g', color = 'forestgreen') 
        plt.errorbar(MJD[FLT=='r'], FLUXCAL[FLT=='r'], FLUXCALERR[FLT=='r'], capsize = 4, label='r', color = 'coral')
        plt.errorbar(MJD[FLT=='i'], FLUXCAL[FLT=='i'], FLUXCALERR[FLT=='i'], capsize = 4, label='i', color = 'indianred')
        plt.errorbar(MJD[FLT=='z'], FLUXCAL[FLT=='z'], FLUXCALERR[FLT=='z'], capsize = 4, label='z', color = 'gray')
        plt.title('%s no host-galaxy photo-z; SNTYPE: 1' % SNIa_list['SNIa List'][i]) #adjust for other types
        plt.xlabel('Modified Julian Date')
        plt.ylabel('Calibrated Flux')
        plt.legend()
        plot_num += 1
        i+=1
        if i>=834: break #adjust for other types
    pdf.savefig(fig)

pdf.close()
