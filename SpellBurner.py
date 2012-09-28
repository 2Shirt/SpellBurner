# Burning Wheel - Spell Burner
# By 2Shirt (Alan Mason)
#
# Version 0.07a
from tkinter import *
from tkinter import ttk
from math import ceil, floor, log

facets = {
	'Element': {
		'Air': {'Actions:': 4, 'Ob': 2, 'ResCost': 10},
		'Anima': {'Actions:': 5, 'Ob': 5, 'ResCost': 12},
		'Arcana': {'Actions:': 10, 'Ob': 4, 'ResCost': 13},
		'Earth': {'Actions:': 6, 'Ob': 1, 'ResCost': 8},
		'Fire': {'Actions:': 5, 'Ob': 2, 'ResCost': 10},
		'Heaven': {'Actions:': 8, 'Ob': 3, 'ResCost': 10},
		'Water': {'Actions:': 3, 'Ob': 2, 'ResCost': 9},
		'White': {'Actions:': 7, 'Ob': 4, 'ResCost': 11},
	},

	'Impetus': {
		'Control': {'Actions:': 16, 'Ob': 5, 'ResCost': 5},
		'Create': {'Actions:': 32, 'Ob': 6, 'ResCost': 6},
		'Destroy': {'Actions:': 2, 'Ob': 2, 'ResCost': 3},
		'Enhance': {'Actions:': 12, 'Ob': 4, 'ResCost': 4},
		'Influence': {'Actions:': 4, 'Ob': 3, 'ResCost': 3},
		'Tax': {'Actions:': 1, 'Ob': 1, 'ResCost': 2},
		'Transmute (Control)': {'Actions:': 25, 'Ob': 8, 'ResCost': 7},
		'Transmute (Create)': {'Actions:': 25, 'Ob': 9, 'ResCost': 7},
		'Transmute (Destroy)': {'Actions:': 25, 'Ob': 5, 'ResCost': 7},
		'Transmute (Enhance)': {'Actions:': 25, 'Ob': 7, 'ResCost': 7},
		'Transmute (Influence)': {'Actions:': 25, 'Ob': 6, 'ResCost': 7},
		'Transmute (Tax)': {'Actions:': 25, 'Ob': 4, 'ResCost': 7},
	},

	'Origin': {
		'Personal': {'Actions:': 1, 'Ob': 0, 'ResCost': 0},
		'Presence': {'Actions:': 2, 'Ob': 2, 'ResCost': 2},
		'Sight': {'Actions:': 4, 'Ob': 4, 'ResCost': 4},
	},

	'Duration': {
		'Instantaneous': {'Actions:': 1, 'Ob': 0, 'ResCost': 0},
		'Sustained': {'Actions:': 2, 'Ob': 2, 'ResCost': 2},
		'Elapsed Time (Seconds)': {'Actions:': 2, 'Ob': 1, 'ResCost': 2},
		'Elapsed Time (Exchanges)': {'Actions:': 6, 'Ob': 2, 'ResCost': 4},
		'Elapsed Time (Minutes)': {'Actions:': 8, 'Ob': 3, 'ResCost': 5},
		'Elapsed Time (Hours)': {'Actions:': 12, 'Ob': 4, 'ResCost': 7},
		'Elapsed Time (Days)': {'Actions:': 24, 'Ob': 5, 'ResCost': 8},
		'Elapsed Time (Months)': {'Actions:': 43, 'Ob': 7, 'ResCost': 9},
		'Elapsed Time (Years)': {'Actions:': 81, 'Ob': 9, 'ResCost': 10},
		'Permanent': {'Actions:': 500, 'Ob': 10, 'ResCost': 100},
	},

	'Area of Effect': {
		'Caster': {'Actions:': 1, 'Ob': 0, 'ResCost': 0},
		'Single Target': {'Actions:': 2, 'Ob': 1, 'ResCost': 2},
		'Presence': {'Actions:': 3, 'Ob': 2, 'ResCost': 3},
		'Half Presence': {'Actions:': 3, 'Ob': 1, 'ResCost': 2},
		'Double Presence': {'Actions:': 6, 'Ob': 4, 'ResCost': 4},
		'Natural Effect': {'Actions:': 4, 'Ob': 3, 'ResCost': 4},
		'Half Natural Effect': {'Actions:': 3, 'Ob': 2, 'ResCost': 3},
		'Double Natural Effect': {'Actions:': 8, 'Ob': 6, 'ResCost': 8},
		'Area (Paces)': {'Actions:': 4, 'Ob': 2, 'ResCost': 3},
		'Area (Tens of Paces)': {'Actions:': 6, 'Ob': 4, 'ResCost': 5},
		'Area (Hundreds of Paces)': {'Actions:': 8, 'Ob': 6, 'ResCost': 6},
		'Area (Miles)': {'Actions:': 10, 'Ob': 8, 'ResCost': 8},
		'Area (Tens of Miles)': {'Actions:': 15, 'Ob': 9, 'ResCost': 9},
		'Area (Hundreds of Miles)': {'Actions:': 20, 'Ob': 10, 'ResCost': 10},
	},
}

def roundMinOne(x):
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

class Facet():
	def updateOptions(self, *args):
		try:
			self.optionSelect['values'] = sorted(facets[self.type.get()].keys())
		except KeyError:
			pass
		
	def updateStats(self, *args):
		if self.option.get() == 'Anima':
			try:
				self.obValueLabel.destroy()
			except AttributeError:
				pass
			self.ob.set(5)
			self.obCombobox = ttk.Combobox(self.frame, textvariable=self.ob, width=2)
			self.obCombobox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
			self.obCombobox.state(['readonly'])
			self.obCombobox.bind('<<ComboboxSelected>>', self.frame.updateAll)
			self.obCombobox.grid(column=6, row=self.row, sticky=W)
		else:
			try:
				self.obCombobox.destroy()
			except AttributeError:
				pass
			self.ob.set(facets[self.type.get()][self.option.get()]['Ob'])
			self.obValueLabel = ttk.Label(self.frame, textvariable=self.ob)
			self.obValueLabel.grid(column=6, row=self.row, sticky=W)
		self.actions.set(facets[self.type.get()][self.option.get()]['Actions:'])
		self.frame.updateAll()
		
	def createWidgets(self):
		self.typeSelect = ttk.Combobox(self.frame, textvariable=self.type, width=15)
		self.typeSelect['values'] = sorted(facets.keys())
		self.typeSelect.state(['readonly'])
		self.typeSelect.bind('<<ComboboxSelected>>', self.updateOptions)
		self.typeSelect.grid(column=1, row=self.row, columnspan=2, sticky=(W, E))
		
		self.optionSelect = ttk.Combobox(self.frame, textvariable=self.option)
		self.optionSelect.state(['readonly'])
		self.optionSelect.bind('<<ComboboxSelected>>', self.updateStats)
		self.optionSelect.grid(column=3, row=self.row, columnspan=2, sticky=(W, E))
		
		self.obLabel = ttk.Label(self.frame, text='Ob:', width=3)
		self.obLabel.grid(column=5, row=self.row, sticky=W)
		
		self.obValueLabel = ttk.Label(self.frame, textvariable=self.ob, width=6)
		self.obValueLabel.grid(column=6, row=self.row, sticky=W)
		
		self.actionsLabel = ttk.Label(self.frame, text='Actions:')
		self.actionsLabel.grid(column=7, row=self.row, sticky=W)
		
		self.actionsValueLabel = ttk.Label(self.frame, textvariable=self.actions, width=3)
		self.actionsValueLabel.grid(column=8, row=self.row, sticky=W)

	def getActions(self):
		return float(self.actions.get())

	def getOb(self):
		return float(self.ob.get())
		
	def __init__(self, frame, row, default=''):
		self.frame = frame
		self.row = row
		self.actions = StringVar()
		self.actions.set('0')
		self.ob = StringVar()
		self.ob.set('0')
		self.option = StringVar()
		self.type = StringVar()
		self.type.set(default)
		self.createWidgets()
		self.updateOptions()

class Distiller():
	def updateStats(self, *args):
		self.obTmp = 0
		self.actionsTmp = 0
		for x in self.tobedistilled:
			try:
				self.obTmp += x.getOb()
				self.actionsTmp += x.getActions()
			except AttributeError:
				for y in x:
					self.obTmp += y.getOb()
					self.actionsTmp += y.getActions()
		if self.round is 'true':
			self.ob.set(str(roundMinOne(self.obTmp/2)))
			self.actions.set(str(roundMinOne(self.actionsTmp/2)))
		else:
			self.ob.set(str(self.obTmp/2))
			self.actions.set(str(self.actionsTmp/2))
	
	def createWidgets(self):
		ttk.Separator(self.frame, orient=HORIZONTAL).grid(column=1, row=self.row, columnspan=8, sticky=(W, E))
		
		self.titleLabel = ttk.Label(self.frame, text=self.title, justify='right')
		self.titleLabel.grid(column=4, row=self.row + 1, sticky=(W, E))
		
		self.obLabel = ttk.Label(self.frame, text='Ob:')
		self.obLabel.grid(column=5, row=self.row + 1, sticky=(W, E))
		
		self.obValueLabel = ttk.Label(self.frame, textvariable=self.ob)
		self.obValueLabel.grid(column=6, row=self.row + 1, sticky=(W, E))
		
		self.actionsLabel = ttk.Label(self.frame, text='Actions:')
		self.actionsLabel.grid(column=7, row=self.row + 1, sticky=(W, E))
		
		self.actionsValueLabel = ttk.Label(self.frame, textvariable=self.actions)
		self.actionsValueLabel.grid(column=8, row=self.row + 1, sticky=(W, E))
		
		ttk.Separator(self.frame, orient=HORIZONTAL).grid(column=1, row=self.row + 2, columnspan=8, sticky=(W, E))

	def getActions(self):
		return float(self.actions.get())

	def getOb(self):
		return float(self.ob.get())
	
	def __init__(self, frame, row, title, tobedistilled, round='false', *args):
		self.frame = frame
		self.row = row
		self.title = title
		self.tobedistilled = tobedistilled
		self.round = round
		self.actions = StringVar()
		self.ob = StringVar()
		self.createWidgets()
		self.updateStats()

class MajorisSigil():
	
	def addSigil(self, *args):
		self.addButton.destroy()
		self.frame.addSigil()
	
	def toggleSigil(self, *args):
		if self.enabled.get():
			self.ob.set('1')
			self.obCombobox.state(['!disabled'])
			self.obCombobox['values'] = ('1', '2')
			self.actionsEntry.state(['!disabled'])
			self.actionsEntry.delete(0,'end')
			self.actionsEntry.insert(0, '10')
		else:
			self.ob.set('')
			self.obCombobox['values'] = ('')
			self.obCombobox.state(['disabled'])
			self.actionsEntry.delete(0,'end')
			self.actionsEntry.state(['disabled'])
		self.frame.updateAll()
	
	def validateMultiplier(self, *args):
		try:
			if (float(self.actionsEntry.get()) < 10):
				self.actionsEntry.delete(0,'end')
				self.actionsEntry.insert(0, '10')
			elif (float(self.actionsEntry.get()) > 100):
				self.actionsEntry.delete(0,'end')
				self.actionsEntry.insert(0, '100')
		except ValueError:
			self.actionsEntry.delete(0,'end')
			self.actionsEntry.insert(0, '10')
		except TypeError:
			self.actionsEntry.delete(0,'end')
			self.actionsEntry.insert(0, '10')
		self.frame.updateAll()
		return 1
	
	def correctMultiplier(self, *args):
		self.frame.updateAll()
	
	def createWidgets(self):
		self.addButton = ttk.Button(self.frame, text='+', command=self.addSigil, width=3)
		self.addButton.grid(column=1, row=self.row)
		
		self.toggle = Checkbutton(self.frame, text='Majoris', command=self.toggleSigil,
			variable=self.enabled, onvalue=True, offvalue=False)
		self.toggle.grid(column=2, row=self.row, sticky=W)
		
		self.obCombobox = ttk.Combobox(self.frame, textvariable=self.ob, width=2)
		self.obCombobox.state(['readonly'])
		self.obCombobox['values'] = ('')
		self.obCombobox.bind('<<ComboboxSelected>>', self.frame.updateAll)
		self.obCombobox.grid(column=3, row=self.row, sticky=W)
		self.obCombobox.state(['disabled'])
		
		self.actionsLabel = ttk.Label(self.frame, text='Multiplier')
		self.actionsLabel.grid(column=4, row=self.row, sticky=W)
		
		self.actionsEntry = ttk.Entry(self.frame, validate='focusout',
			validatecommand=self.validateMultiplier, width=5)
		self.actionsEntry.grid(column=5, row=self.row, sticky=W)
		self.actionsEntry.state(['disabled'])

	def getMultiplier(self):
		if self.enabled.get():
			return float(self.actionsEntry.get())
		else:
			return 1.0

	def getOb(self):
		if self.enabled.get():
			return int(self.ob.get())
		else:
			return 0
		
	
	def __init__(self, frame, row, *args):
		self.frame = frame
		self.row = row
		self.multiplier = StringVar()
		self.enabled = BooleanVar()
		self.enabled.set(False)
		self.ob = StringVar()
		self.createWidgets()

class App(ttk.Frame):
	def addExtraFacet(self, *args):
		if len(self.extraFacets) == 9:
			self.extraFacetButton.destroy()
		self.extraFacets.append(Facet(self, 11+len(self.extraFacets)))
		self.configureGrid()
	
	def addSigil(self, *args):
		self.extraFacetRow = self.extraFacetRow + 1
		if self.extraFacetRow < 36:
			self.majorisSigils.append(MajorisSigil(self, self.extraFacetRow))
		self.configureGrid()
	
	def generateRange(self, limit, *args):
		self.rangeList = []
		for i in range(limit):
			self.rangeList.append(str(i))
		return self.rangeList
	
	def configureGrid(self, *args):
		for child in self.winfo_children(): child.grid_configure(padx=2, pady=2)
	
	def updateAll(self, *args):
		# Distillations
		self.distiller1.updateStats()
		self.distiller2.updateStats()
		self.distiller3.updateStats()
		
		# After Final Distillation
		self.finalObValue = roundMinOne(self.distiller3.getOb())
		self.finalActionsValue = roundMinOne(self.distiller3.getActions())
		
		# Cap Sigil
		if self.capValue.get():
			self.finalObValue -= 1
		
		# Minoris Sigil(s)
		try:
			self.finalObValue -= int(self.minorisValue.get())
		except ValueError:
			pass
		
		# Majoris Sigil(s)
		for s in self.majorisSigils:
			self.finalObValue += s.getOb()
			self.finalActionsValue *= s.getMultiplier()
		
		# Extention(s)
		try:
			self.finalObValue -= 1*int(self.extendValue.get())
			self.finalActionsValue *= 5**int(self.extendValue.get())
		except ValueError:
			pass
		
		# Compression(s)
		cTest = self.finalActionsValue
		curCompress = int(self.compressValue.get())
		try:
			if curCompress > 0:
				self.finalObValue += 1*curCompress
				self.finalActionsValue = roundMinOne(ceil(self.finalActionsValue*(1/2)**curCompress))
		except ValueError:
			pass
		
		# Final Spell Stats
		if self.capValue.get():
			self.finalOb.set(roundMinOne(self.finalObValue))
		else:
			self.finalOb.set(str(roundMinOne(self.finalObValue)) + '^')
		self.finalActions.set(int(self.finalActionsValue))
		self.configureGrid()
		
		# Limit selection: Minoris Sigil(s)
		origOb = roundMinOne(self.distiller3.getOb())
		curMinoris = int(self.minorisValue.get())
		try:
			# Limit minoris sigil amount
			if self.finalObValue == 1:
				limit = curMinoris + 1
			elif 0 < self.finalObValue <= origOb - 1 - curMinoris:
				limit = self.finalObValue + curMinoris
			elif origOb - 1 - curMinoris < self.finalObValue:
				limit = origOb
			else:
				limit = 1 # Not sure what this case is...
			if limit <= 0:
				limit = 1
			self.minorisCombobox['values'] = tuple(range(int(limit)))
		except ValueError:
			pass
		del curMinoris
		
		# Limit selection: Extention(s)
		try:
			# Limit number of extentions
			max = origOb - roundUp(origOb / 2)
			if self.finalObValue > max:
				limit = max + 1
			elif self.finalObValue > 1:
				if int(self.extendValue.get()) == max:
					limit = max + 1
				else:
					limit = self.finalObValue
			elif int(self.extendValue.get()) > 0:
				limit = int(self.extendValue.get()) + 1
			else:
				limit = 1
			self.extendCombobox['values'] = tuple(range(int(limit)))
			del max
		except ValueError:
			pass
		
		# Limit selection: Compression(s)
		try:
			# Limit number of compressions
			if self.finalActionsValue == 1:
				if roundMinOne(self.distiller3.getActions()) == 1:
					limit = 1
				else:
					for x in range(curCompress+1):
						cTest = ceil(cTest/2)
						#print('cTest (', x, ') ', cTest)
						if cTest == 1:
							#print('\tSet limit: ', x + 2)
							limit = x + 2
							break
						else:
							# VERY WRONG, SHOULDN'T HAPPEN
							limit = 1
			else:
				limit = ceil(log(1/self.finalActionsValue, 1/2)) + 1 + curCompress
			self.compressCombobox['values'] = tuple(range(int(limit)))
		except ValueError:
			pass
		del limit
		del origOb
		del curCompress
		
	def createWidgets(self):
		# 1st Distillation
		self.facet1 = Facet(self, 0, 'Element')
		self.facet2 = Facet(self, 1, 'Impetus')
		
		self.distiller1 = Distiller(self, 2, '1st Distillation',
			(self.facet1, self.facet2)
		)
		
		# 2nd Distillation
		self.facet3 = Facet(self, 5, 'Origin')
		self.facet4 = Facet(self, 6, 'Duration')
		
		self.distiller2 = Distiller(self, 7, '2nd Distillation',
			(self.facet3, self.facet4)
		)
		
		# 3rd Distillation
		self.facet5 = Facet(self, 10, 'Area of Effect')
		
		self.extraFacetButton = ttk.Button(self, text='+', command=self.addExtraFacet, width=3)
		self.extraFacetButton.grid(column=1, row=19)
		
		self.distiller3 = Distiller(self, 20, 'Final Distillation',
			(self.distiller1, self.distiller2, self.facet5, self.extraFacets),
			round='true'
		)
		
		# Sigils
		ttk.Label(self, text='Sigils').grid(column=1, row=24)
		
		# Adjustments - Cap & Minoris Sigil(S)		
		self.capCheckbutton = Checkbutton(self, text='Cap', command=self.updateAll,
			variable=self.capValue, onvalue=True, offvalue=False)
		self.capCheckbutton.grid(column=2, row=25, sticky=W)
		
		self.minorisLabel = ttk.Label(self, text='Minoris')
		self.minorisLabel.grid(column=4, row=25, sticky=E)
		
		self.minorisCombobox = ttk.Combobox(self, textvariable=self.minorisValue, width=2)
		self.minorisCombobox.state(['readonly'])
		self.minorisCombobox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		self.minorisCombobox.bind('<<ComboboxSelected>>', self.updateAll)
		self.minorisCombobox.grid(column=5, row=25, sticky=W)
		
		# Adjustments - Majoris Sigil(S)
		self.majorisSigils.append(MajorisSigil(self, self.extraFacetRow))
		
		# Adjustments - Compress & Extend		
		self.compressLabel = ttk.Label(self, text='Compressions')
		self.compressLabel.grid(column=2, row=36, sticky=W)
		
		self.compressCombobox = ttk.Combobox(self, textvariable=self.compressValue, width=2)
		self.compressCombobox.state(['readonly'])
		self.compressCombobox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		self.compressCombobox.bind('<<ComboboxSelected>>', self.updateAll)
		self.compressCombobox.grid(column=3, row=36, sticky=W)
		
		self.extendLabel = ttk.Label(self, text='Extentions')
		self.extendLabel.grid(column=4, row=36, sticky=W)
		
		self.extendCombobox = ttk.Combobox(self, textvariable=self.extendValue, width=2)
		self.extendCombobox.state(['readonly'])
		self.extendCombobox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		self.extendCombobox.bind('<<ComboboxSelected>>', self.updateAll)
		self.extendCombobox.grid(column=5, row=36, sticky=W)
		
		# Final Spell Results
		ttk.Separator(self, orient=HORIZONTAL).grid(column=1, row=37, columnspan=8, sticky=(W, E))
		
		self.titleLabel = ttk.Label(self, text='Final Spell Stats', justify='right')
		self.titleLabel.grid(column=4, row=38, sticky=(W, E))
		
		self.obLabel = ttk.Label(self, text='Ob:')
		self.obLabel.grid(column=5, row=38, sticky=(W, E))
		
		self.obValueLabel = ttk.Label(self, textvariable=self.finalOb)
		self.obValueLabel.grid(column=6, row=38, sticky=(W, E))
		
		self.actionsLabel = ttk.Label(self, text='Actions:')
		self.actionsLabel.grid(column=7, row=38, sticky=(W, E))
		
		self.actionsValueLabel = ttk.Label(self, textvariable=self.finalActions)
		self.actionsValueLabel.grid(column=8, row=38, sticky=(W, E))
		
	def __init__(self, master):
		Frame.__init__(self, master)
		self.frame = master
		self.capValue = BooleanVar()
		self.capValue.set(False)
		self.compressValue = StringVar()
		self.compressValue.set(0)
		self.extendValue = StringVar()
		self.extendValue.set(0)
		self.minorisValue = StringVar()
		self.minorisValue.set(0)
		self.extraFacetRow = 26
		self.extraFacets = []
		self.finalOb = StringVar()
		self.finalObValue = 1
		self.finalActions = StringVar()
		self.finalActionsValue = 1
		self.majorisSigils = []
		self.createWidgets()
		self.updateAll()
		self.configureGrid()

root = Tk()
root.title('Spell Burner')
#root.resizable(0, 0)						# disable window resizing
root.resizable(width=FALSE, height=FALSE)	# disable window resizing

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