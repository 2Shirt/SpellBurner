# Burning Wheel - Spell Burner
# By 2Shirt (Alan Mason)
#
# Version 0.03a
from tkinter import *
from tkinter import ttk
from math import floor

facets = {
	'Element': {
		'Air': {'Actions': 4, 'Ob': 2, 'ResCost': 10},
		'Anima': {'Actions': 5, 'Ob': 5, 'ResCost': 12},
		'Arcana': {'Actions': 10, 'Ob': 4, 'ResCost': 13},
		'Earth': {'Actions': 6, 'Ob': 1, 'ResCost': 8},
		'Fire': {'Actions': 5, 'Ob': 2, 'ResCost': 10},
		'Heaven': {'Actions': 8, 'Ob': 3, 'ResCost': 10},
		'Water': {'Actions': 3, 'Ob': 2, 'ResCost': 9},
		'White': {'Actions': 7, 'Ob': 4, 'ResCost': 11},
	},

	'Impetus': {
		'Control': {'Actions': 16, 'Ob': 5, 'ResCost': 5},
		'Create': {'Actions': 32, 'Ob': 6, 'ResCost': 6},
		'Destroy': {'Actions': 2, 'Ob': 2, 'ResCost': 3},
		'Enhance': {'Actions': 12, 'Ob': 4, 'ResCost': 4},
		'Influence': {'Actions': 4, 'Ob': 3, 'ResCost': 3},
		'Tax': {'Actions': 1, 'Ob': 1, 'ResCost': 2},
		'Transmute (Control)': {'Actions': 25, 'Ob': 8, 'ResCost': 7},
		'Transmute (Create)': {'Actions': 25, 'Ob': 9, 'ResCost': 7},
		'Transmute (Destroy)': {'Actions': 25, 'Ob': 5, 'ResCost': 7},
		'Transmute (Enhance)': {'Actions': 25, 'Ob': 7, 'ResCost': 7},
		'Transmute (Influence)': {'Actions': 25, 'Ob': 6, 'ResCost': 7},
		'Transmute (Tax)': {'Actions': 25, 'Ob': 4, 'ResCost': 7},
	},

	'Origin': {
		'Personal': {'Actions': 1, 'Ob': 0, 'ResCost': 0},
		'Presence': {'Actions': 2, 'Ob': 2, 'ResCost': 2},
		'Sight': {'Actions': 4, 'Ob': 4, 'ResCost': 4},
	},

	'Duration': {
		'Instantaneous': {'Actions': 1, 'Ob': 0, 'ResCost': 0},
		'Sustained': {'Actions': 2, 'Ob': 2, 'ResCost': 2},
		'Elapsed Time (Seconds)': {'Actions': 2, 'Ob': 1, 'ResCost': 2},
		'Elapsed Time (Exchanges)': {'Actions': 6, 'Ob': 2, 'ResCost': 4},
		'Elapsed Time (Minutes)': {'Actions': 8, 'Ob': 3, 'ResCost': 5},
		'Elapsed Time (Hours)': {'Actions': 12, 'Ob': 4, 'ResCost': 7},
		'Elapsed Time (Days)': {'Actions': 24, 'Ob': 5, 'ResCost': 8},
		'Elapsed Time (Months)': {'Actions': 43, 'Ob': 7, 'ResCost': 9},
		'Elapsed Time (Years)': {'Actions': 81, 'Ob': 9, 'ResCost': 10},
		'Permanent': {'Actions': 500, 'Ob': 10, 'ResCost': 100},
	},

	'Area of Effect': {
		'Caster': {'Actions': 1, 'Ob': 0, 'ResCost': 0},
		'Single Target': {'Actions': 2, 'Ob': 1, 'ResCost': 2},
		'Presence': {'Actions': 3, 'Ob': 2, 'ResCost': 3},
		'Half Presence': {'Actions': 3, 'Ob': 1, 'ResCost': 2},
		'Double Presence': {'Actions': 6, 'Ob': 4, 'ResCost': 4},
		'Natural Effect': {'Actions': 4, 'Ob': 3, 'ResCost': 4},
		'Half Natural Effect': {'Actions': 3, 'Ob': 2, 'ResCost': 3},
		'Double Natural Effect': {'Actions': 8, 'Ob': 6, 'ResCost': 8},
		'Area (Paces)': {'Actions': 4, 'Ob': 2, 'ResCost': 3},
		'Area (Tens of Paces)': {'Actions': 6, 'Ob': 4, 'ResCost': 5},
		'Area (Hundreds of Paces)': {'Actions': 8, 'Ob': 6, 'ResCost': 6},
		'Area (Miles)': {'Actions': 10, 'Ob': 8, 'ResCost': 8},
		'Area (Tens of Miles)': {'Actions': 15, 'Ob': 9, 'ResCost': 9},
		'Area (Hundreds of Miles)': {'Actions': 20, 'Ob': 10, 'ResCost': 10},
	},
}

def roundBW(x):
	if (floor(x) == 0):
		return 1
	elif (x - floor(x) >= 0.5):
		return floor(x) + 1
	else:
		return floor(x)

def roundDown(x):
	if (floor(x) == 0):
		return 1
	else:
		return floor(x)

def roundUp(x):
	return ceil(x)

class Facet(ttk.Frame):
	def updateOptions(self, *args):
		try:
			self.optionSelect['values'] = sorted(facets[self.type.get()].keys())
		except KeyError:
			pass
		
	def updateStats(self, *args):
		if self.option.get() == 'Anima':
			## Todo ##
			try:
				self.obLabel.destroy()
			except AttributeError:
				pass
			self.ob.set(5)
			self.obCombobox = ttk.Combobox(self.obFrame, textvariable=self.ob, width=2)
			self.obCombobox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
			self.obCombobox.state(['readonly'])
			self.obCombobox.bind('<<ComboboxSelected>>', self.parent.updateAll)
			self.obCombobox.grid(column=1, row=1, sticky=W)
		else:
			try:
				self.obCombobox.destroy()
			except AttributeError:
				pass
			self.ob.set(facets[self.type.get()][self.option.get()]['Ob'])
			self.obLabel = ttk.Label(self.obFrame, textvariable=self.ob)
			self.obLabel.grid(column=1, row=1, sticky=W)
		self.actions.set(facets[self.type.get()][self.option.get()]['Actions'])
		self.parent.updateAll()
		
	def createWidgets(self):
		self.typeSelect = ttk.Combobox(self, textvariable=self.type)
		self.typeSelect['values'] = sorted(facets.keys())
		self.typeSelect.state(['readonly'])
		self.typeSelect.bind('<<ComboboxSelected>>', self.updateOptions)
		self.typeSelect.grid(column=1, row=1, sticky=W)
		
		self.optionSelect = ttk.Combobox(self, textvariable=self.option)
		self.optionSelect.state(['readonly'])
		self.optionSelect.bind('<<ComboboxSelected>>', self.updateStats)
		self.optionSelect.grid(column=2, row=1, sticky=W)
		
		self.obFrame = ttk.Labelframe(self, text='Ob')
		self.obFrame.grid(column=3, row=1, sticky=W)
		self.obLabel = ttk.Label(self.obFrame, textvariable=self.ob)
		self.obLabel.grid(column=1, row=1, sticky=W)
		
		self.actionsFrame = ttk.Labelframe(self, text='Actions')
		self.actionsFrame.grid(column=4, row=1, sticky=W)
		self.actionsLabel = ttk.Label(self.actionsFrame, textvariable=self.actions)
		self.actionsLabel.grid(column=1, row=1, sticky=W)

	def getActions(self):
		return float(self.actions.get())

	def getOb(self):
		return float(self.ob.get())
		
	def __init__(self, master, default=''):
		Frame.__init__(self, master)
		self.parent = master
		self.actions = StringVar()
		self.actions.set('0')
		self.ob = StringVar()
		self.ob.set('0')
		self.option = StringVar()
		self.type = StringVar()
		self.type.set(default)
		self.createWidgets()
		self.updateOptions()
		for child in self.winfo_children(): child.grid_configure(padx=5, pady=0)

class Distiller(ttk.Frame):
	def updateStats(self, *args):
		self.obTmp = 0
		self.actionsTmp = 0
		for x in self.tobedistilled:
			self.obTmp += x.getOb()
			self.actionsTmp += x.getActions()
		if self.round is 'true':
			self.ob.set(str(roundBW(self.obTmp/2)))
			self.actions.set(str(roundBW(self.actionsTmp/2)))
		else:
			self.ob.set(str(self.obTmp/2))
			self.actions.set(str(self.actionsTmp/2))
	
	def createWidgets(self):
		self.titleLabel = ttk.Label(self, text=self.title, justify='right')
		self.titleLabel.grid(column=1, row=1, columnspan=2, sticky=W)
		
		self.obFrame = ttk.Labelframe(self, text='Ob')
		self.obFrame.grid(column=3, row=1, sticky=W)
		self.obLabel = ttk.Label(self.obFrame, textvariable=self.ob)
		self.obLabel.grid(column=1, row=1, sticky=W)
		
		self.actionsFrame = ttk.Labelframe(self, text='Actions')
		self.actionsFrame.grid(column=4, row=1, sticky=W)
		self.actionsLabel = ttk.Label(self.actionsFrame, textvariable=self.actions)
		self.actionsLabel.grid(column=1, row=1, sticky=W)

	def getActions(self):
		return float(self.actions.get())

	def getOb(self):
		return float(self.ob.get())
	
	def __init__(self, master, title, tobedistilled, round='false', *args):
		Frame.__init__(self, master)
		self.parent = master
		self.title = title
		self.tobedistilled = tobedistilled
		self.round = round
		self.actions = StringVar()
		self.ob = StringVar()
		self.createWidgets()
		self.updateStats()
		for child in self.winfo_children(): child.grid_configure(padx=5, pady=0)

class MajorisSigil(ttk.Frame):
	
	def addSigil(self, *args):
		self.addButton.destroy()
		self.parent.addSigil()
	
	def toggleSigil(self, *args):
		self.ob.set('1')
		self.obCombobox['values'] = ('1', '2')
		self.obCombobox.state(['!disabled'])
		self.actionsEntry.state(['!disabled'])
		self.actionsEntry.delete(0,'end')
		self.actionsEntry.insert(0, '10')
	
	def validateMultiplier(self, *args):
		try:
			if (float(self.actionsEntry.get()) < 10):
				print('<10')
				self.actionsEntry.delete(0,'end')
				self.actionsEntry.insert(0, '10')
			elif (float(self.actionsEntry.get()) > 100):
				print('>100')
				self.actionsEntry.delete(0,'end')
				self.actionsEntry.insert(0, '100')
		except ValueError:
			print('ValueError')
			self.actionsEntry.delete(0,'end')
			self.actionsEntry.insert(0, '10')
		except TypeError:
			print('TypeError')
			self.actionsEntry.delete(0,'end')
			self.actionsEntry.insert(0, '10')
		return 1
	
	def correctMultiplier(self, *args):
		pass
	
	def createWidgets(self):		
		self.toggle = Checkbutton(self, text='Majoris Sigil', command=self.toggleSigil,
			variable=self.enabled, onvalue='1', offvalue='0')
		self.toggle.grid(column=1, row=1, sticky=W)
		
		self.obCombobox = ttk.Combobox(self, textvariable=self.ob)
		self.obCombobox.state(['readonly'])
		self.obCombobox['values'] = ('')
		self.obCombobox.bind('<<ComboboxSelected>>', self.parent.updateAll)
		self.obCombobox.grid(column=2, row=1, sticky=W)
		self.obCombobox.state(['disabled'])
		
		self.actionsEntry = ttk.Entry(self, validate='focusout',
			validatecommand=self.validateMultiplier, width=4)
		self.actionsEntry.grid(column=3, row=1, sticky=W)
		self.actionsEntry.state(['disabled'])
		
		self.addButton = ttk.Button(self, text='+', command=self.addSigil)
		self.addButton.grid(column=4, row=1, sticky=W)

	def getMultiplier(self):
		if self.enabled == '1':
			return float(self.actionsEntry.get())
		else:
			return 1.0

	def getOb(self):
		if self.enabled == '1':
			return int(self.ob.get())
		else:
			return 0
		
	
	def __init__(self, master, *args):
		Frame.__init__(self, master)
		self.parent = master
		self.multiplier = StringVar()
		self.enabled = StringVar()
		self.enabled.set('0')
		self.ob = StringVar()
		self.createWidgets()
#		self.updateStats()
		for child in self.winfo_children(): child.grid_configure(padx=5, pady=0)

class App(ttk.Frame):
	def addSigil(self, *args):
		self.i = self.i + 1
		if self.i < 17:
			self.sigils.append(MajorisSigil(self))
			self.sigils[-1].grid(column=1, row=self.i, sticky=W)
	
	def updateAll(self, *args):
		#Distillations
		self.distiller1.updateStats()
		self.distiller2.updateStats()
		self.distiller3.updateStats()
		#Final Spell
		#self.capValue
#		self.minorisCombobox['values'] # set current limit
		
	def createWidgets(self):
		# 1st Distillation
		self.facet1 = Facet(self, 'Element')
		self.facet1.grid(column=1, row=1, sticky=W)
		self.facet2 = Facet(self, 'Impetus')
		self.facet2.grid(column=1, row=2, sticky=W)
		
		self.distiller1 = Distiller(self, '1st Distillation',
			(self.facet1, self.facet2)
		)
		self.distiller1.grid(column=1, row=3, sticky=W)
		
		# 2nd Distillation
		self.facet3 = Facet(self, 'Origin')
		self.facet3.grid(column=1, row=4, sticky=W)
		self.facet4 = Facet(self, 'Duration')
		self.facet4.grid(column=1, row=5, sticky=W)
		
		self.distiller2 = Distiller(self, '2nd Distillation',
			(self.facet3, self.facet4)
		)
		self.distiller2.grid(column=1, row=6, sticky=W)
		
		# 3rd Distillation
		self.facet5 = Facet(self, 'Area of Effect')
		self.facet5.grid(column=1, row=7, sticky=W)
		self.facet6 = Facet(self)
		self.facet6.grid(column=1, row=8, sticky=W)
		self.facet7 = Facet(self)
		self.facet7.grid(column=1, row=9, sticky=W)
		
		self.distiller3 = Distiller(self, 'Final Distillation',
			(self.distiller1, self.distiller2, self.facet5, self.facet6, self.facet7),
			round='true'
		)
		self.distiller3.grid(column=1, row=10, sticky=W)
		
		# Adjustments - Cap & Minoris Sigil(S)
		self.frameCapMinoris = ttk.Frame(self)
		self.frameCapMinoris.grid(column=1, row=11, sticky=(N, W, E, S))
		self.frameCapMinoris.columnconfigure(0, weight=1)
		self.frameCapMinoris.rowconfigure(0, weight=1)
		
		self.capCheckbutton = Checkbutton(self.frameCapMinoris, text='Cap', command=self.updateAll,
			variable=self.capValue, onvalue='1', offvalue='0')
		self.capCheckbutton.grid(column=1, row=1, sticky=W)
		
		self.minorisLabel = ttk.Label(self.frameCapMinoris, text='Minoris Sigils')
		self.minorisLabel.grid(column=3, row=1, sticky=E)
		
		self.minorisCombobox = ttk.Combobox(self.frameCapMinoris, textvariable=self.minorisValue)
		self.minorisCombobox.state(['readonly'])
		self.minorisCombobox['values'] = ('0')
#		self.minorisCombobox.bind('<<ComboboxSelected>>', self.updateStats)
		self.minorisCombobox.grid(column=4, row=1, sticky=E)
		
		# Adjustments - Majoris Sigil(S)
		self.i = self.i + 1
		self.sigils.append(MajorisSigil(self))
		self.sigils[-1].grid(column=1, row=self.i, sticky=W)
		
		# Adjustments - Compress & Extend
		self.frameCompressExtend = ttk.Frame(self)
		self.frameCompressExtend.grid(column=1, row=17, sticky=(N, W, E, S))
		self.frameCompressExtend.columnconfigure(0, weight=1)
		self.frameCompressExtend.rowconfigure(0, weight=1)
		
		self.compressLabel = ttk.Label(self.frameCompressExtend, text='Compressions')
		self.compressLabel.grid(column=1, row=1, sticky=W)
		
		self.compressCombobox = ttk.Combobox(self.frameCompressExtend, textvariable=self.compressValue)
		self.compressCombobox.state(['readonly'])
		self.compressCombobox['values'] = ('0')
#		self.compressCombobox.bind('<<ComboboxSelected>>', self.updateStats)
		self.compressCombobox.grid(column=2, row=1, sticky=W)
		
		self.extendLabel = ttk.Label(self.frameCompressExtend, text='Extentions')
		self.extendLabel.grid(column=3, row=1, sticky=W)
		
		self.extendCombobox = ttk.Combobox(self.frameCompressExtend, textvariable=self.extendValue)
		self.extendCombobox.state(['readonly'])
		self.extendCombobox['values'] = ('0')
#		self.extendCombobox.bind('<<ComboboxSelected>>', self.updateStats)
		self.extendCombobox.grid(column=4, row=1, sticky=W)
		
	def __init__(self, master):
		Frame.__init__(self, master)
		self.parent = master
		self.capValue = StringVar()
		self.capValue.set('0')
		self.compressValue = StringVar()
		self.extendValue = StringVar()
		self.minorisValue = StringVar()
		self.i = 11
		self.sigils = []
		self.createWidgets()
		self.updateAll()
		for child in self.winfo_children(): child.grid_configure(padx=5, pady=2)

root = Tk()
root.title('Spell Burner')

app = App(root)
app.grid(column=0, row=0, sticky=(N, W, E, S))
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

root.mainloop()


#=Element=
#Name	Ob	Act	Res
#Air		2	4	10
#Anima*	0	5	12 # Ob = Target Stat
#Anima	5	5	12
#Arcana	4	10	13
#Earth	1	6	8
#Fire	2	5	10
#Heaven	3	8	10
#Water	2	3	9
#White	4	7	11

#=Impetus=
#Name			Ob	Act	Res
#Control			5	16	5
#Create			6	32	6
#Destroy			2	2	3
#Enhance			4	12	4
#Influence		3	4	3
#Tax				1	1	2
#Transmute-Cntl	8	25	7
#Transmute-Crea	9	25	7
#Transmute-Dstr	5	25	7
#Transmute-Enhc	7	25	7
#Transmute-Infl	6	25	7
#Transmute-Tax	4	25	7

#=Origin=
#Name		Ob	Act	Res
#Personal	0	1	0
#Presence	2	2	2
#Sight		4	4	4

#=Duration=
#Name			Ob	Act	Res
#Instantaneous	0	1	0
#Sustained		2	2	2
#E.Time-Seconds	1	2	2
#E.TimeExchanges	2	6	4
#E.Time-Minutes	3	8	5
#E.Time-Hours	4	12	7
#E.Time-Days		5	24	8
#E.Time-Months	7	43	9
#E.Time-Years	9	81	10
#Permanent		10	500	100

#=Area of Effect=
#Name				Ob	Act	Res
#Caster				0	1	0
#Single Target		1	2	2
#Presence			2	3	3
#1/2 Presence		1	3	2
#2x Presence			4	6	4
#Natural Effect		3	4	4
#1/2 Natural Ef.		2	3	3
#2x Natural Eff.		6	8	8
#M.Area-Paces		2	4	3
#M.Area-Paces (10s)	4	6	5
#M.Area-Paces (100s)	6	8	6
#M.Area-Miles		8	10	8
#M.Area-Miles (10s)	9	15	9
#M.Area-Miles (100s)	10	20	10