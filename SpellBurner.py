# Burning Wheel - Spell Burner
# By 2Shirt (Alan Mason)
#
# Version 0.09a
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

def roundMath(x):
	if (x - floor(x) >= 0.5):
		return floor(x) + 1
	else:
		return floor(x)

def roundDownMinOne(x):
	if (floor(x) == 0):
		return 1
	else:
		return floor(x)

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
			self.ob.set(str(roundMath(self.obTmp/2)))
			self.actions.set(str(roundMath(self.actionsTmp/2)))
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
	
	def generateRange(self, min, max, *args):
		self.rangeList = []
		if min > max:
			# Uh....
			return [0]
		elif min == max:
			return [min]
		else:
			for i in range(min, max+1):
				self.rangeList.append(str(i))
			return self.rangeList
	
	def configureGrid(self, *args):
		for child in self.winfo_children(): child.grid_configure(padx=2, pady=2)
	
	def updateSpellStats(self, *args):
		# Init Variables
		if self.capValue.get():
			self.numCap = 1
		else:
			self.numCap = 0
		# Compressions
		self.numCs = int(self.compressValue.get())
		# Extensions
		self.numEs = int(self.extendValue.get())
		# Minoris
		self.numMin = int(self.minorisValue.get())
		# majoris
		self.majActTotal = 1
		self.majObTotal = 0
		for s in self.majorisSigils:
			self.majObTotal += s.getOb()
			self.majActTotal *= s.getMultiplier()
		# After Final Distillation
		self.subTotalAct = roundMath(self.distiller3.getActions())
		self.subTotalOb = roundMath(self.distiller3.getOb())
		# Before rounding
		self.preAct = max(1, self.subTotalAct)*self.majActTotal*0.5**self.numCs
		self.preOb = self.subTotalOb
		self.preOb -= self.numCap
		self.preOb -= self.numMin
		self.preOb += self.majObTotal
		self.preOb -= self.numEs
		self.preOb += self.numCs
		# After rounding
		self.postAct = ceil(self.preAct)*5**self.numEs
		self.postOb = max(1,self.preOb)
		# current limits
		self.maxCs = 10
		self.minCs = 0
		self.maxEs = 10
		self.minEs = 0
		self.maxMin = 10
		self.minMin = 0
		# Final Spell valid?
		self.valid = True
		
		# Find Actions-based limits
		self.minEs = max(0, self.numEs - floor((self.postAct - 1)/5))
		if self.preAct > 0.5:
			self.maxCs = min(10, ceil(log(1/self.preAct,0.5)) + self.numCs)
		elif self.preAct == 0.5:
			self.valid = False
			self.maxCs = numCs - 1
		else: #self.preAct < 0.5
			self.valid = False
			if self.numEs > 0:
				self.maxCs = max(0, self.numCs - ceil(log(1/(2*self.postAct),2)))
			else:
				self.maxCs = max(0, self.numCs - ceil(log(1/(2*self.preAct),2)))
		
		# Find Ob-based limits
		if self.preOb < 1:
			self.valid = False
			self.minCs = min(10, self.numCs + abs(self.preOb) + 1)
			self.maxEs = max(0, self.numEs - abs(self.preOb) - 1)
			self.maxMin = max(0, self.numMin - abs(self.preOb) - 1)
		elif self.preOb == 1:
			self.maxEs = min(10, self.preOb - ceil(self.subTotalOb/2) + self.numEs)
			self.maxMin = min(10, self.preOb - 1 + self.numMin)
			self.minCs = max(0, self.numCs)
		else: # self.preOb > 1
			self.maxEs = min(10, self.preOb - ceil(self.subTotalOb/2) + self.numEs)
			self.maxMin = min(10, self.preOb - 1 + self.numMin)
			self.minCs = max(0, min(10, self.numCs - self.preOb + 1))
		
		# Set limits
		if self.numCap == 0:
			self.capValue.set(False)
		self.minorisCombobox['values'] = self.generateRange(self.minMin, self.maxMin)
		self.compressCombobox['values'] = self.generateRange(self.minCs, self.maxCs)
		self.extendCombobox['values'] = self.generateRange(self.minEs, self.maxEs)
		
		# Misc Checks
		if self.preOb < ceil(self.subTotalOb/2):
			if self.numEs > self.preOb - ceil(self.subTotalOb/2) + self.numEs >= 0:
				self.valid = False
		
		# Set Stats
		if self.numCap == 0:
			self.finalOb.set(str(self.postOb) + '^')
		else:
			self.finalOb.set(self.postOb)
		self.finalActions.set(self.postAct)
		if self.valid:
			self.warningLabelText.set(' ')
		else:
			self.warningLabelText.set('[HOUSE RULED]')
		self.configureGrid()
	
	def updateAll(self, *args):
		# Distillations
		self.distiller1.updateStats()
		self.distiller2.updateStats()
		self.distiller3.updateStats()
		
		# Final Spell
		self.updateSpellStats()
		
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
		
		self.extendLabel = ttk.Label(self, text='Extensions')
		self.extendLabel.grid(column=4, row=36, sticky=W)
		
		self.extendCombobox = ttk.Combobox(self, textvariable=self.extendValue, width=2)
		self.extendCombobox.state(['readonly'])
		self.extendCombobox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		self.extendCombobox.bind('<<ComboboxSelected>>', self.updateAll)
		self.extendCombobox.grid(column=5, row=36, sticky=W)
		
		# Final Spell Results
		ttk.Separator(self, orient=HORIZONTAL).grid(column=1, row=37, columnspan=8, sticky=(W, E))
		
		self.warningLabelText = StringVar()
		self.warningLabelText.set(' ')
		self.warningLabel = ttk.Label(self, textvariable=self.warningLabelText, justify='right')
		self.warningLabel.grid(column=1, row=38, columnspan=2, sticky=(W, E))
		
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
