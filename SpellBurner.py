# Burning Wheel - Spell Burner
# By 2Shirt (Alan Mason)
#
# Version 0.02a
from tkinter import *
from tkinter import ttk

facets = {
	'Elements': {
		'Air': {'Actions': 4, 'Ob': 2, 'ResCost': 10},
		'Anima (Target)': {'Actions': 5, 'Ob': 0, 'ResCost': 12},
		'Anima': {'Actions': 5, 'Ob': 5, 'ResCost': 12},
		'Arcana': {'Actions': 10, 'Ob': 4, 'ResCost': 13},
		'Earth': {'Actions': 6, 'Ob': 1, 'ResCost': 8},
		'Fire': {'Actions': 5, 'Ob': 2, 'ResCost': 10},
		'Heaven': {'Actions': 8, 'Ob': 3, 'ResCost': 10},
		'Water': {'Actions': 3, 'Ob': 2, 'ResCost': 9},
		'White': {'Actions': 7, 'Ob': 4, 'ResCost': 11},
	},

	'Impeti': {
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

	'Origins': {
		'Personal': {'Actions': 1, 'Ob': 0, 'ResCost': 0},
		'Presence': {'Actions': 2, 'Ob': 2, 'ResCost': 2},
		'Sight': {'Actions': 4, 'Ob': 4, 'ResCost': 4},
	},

	'Durations': {
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

	'Areas of Effect': {
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

class Facet(ttk.Frame):
	def updateOptions(self, *args):
		self.optionSelect['values'] = sorted(facets[self.type.get()].keys())
	def updateStats(self, *args):
		self.ob.set(facets[self.type.get()][self.option.get()]['Ob'])
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
		
	def __init__(self, master):
		Frame.__init__(self, master)
		self.parent = master
		self.actions = StringVar()
		self.actions.set('0')
		self.ob = StringVar()
		self.ob.set('0')
		self.option = StringVar()
		self.type = StringVar()
		self.createWidgets()
		for child in self.winfo_children(): child.grid_configure(padx=5, pady=0)

class Distiller(ttk.Frame):
	def updateStats(self, *args):
		self.obTmp = 0
		self.actionsTmp = 0
		for x in self.tobedistilled:
#			print(x.getOb())
#			print(x.getActions())
			self.obTmp += x.getOb()
			self.actionsTmp += x.getActions()
#			print(self.obTmp)
#			print(self.actionsTmp)
		self.ob.set(str(self.obTmp/2))
		self.actions.set(str(self.actionsTmp/2))
#		print(self.ob)
#		print(self.actions)
#		print('----------------------')
	
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
	
	def __init__(self, master, title, tobedistilled, *args):
		Frame.__init__(self, master)
		self.parent = master
		self.title = title
		self.tobedistilled = tobedistilled
		self.actions = StringVar()
		self.ob = StringVar()
		self.createWidgets()
		self.updateStats()
		for child in self.winfo_children(): child.grid_configure(padx=5, pady=0)

class App(ttk.Frame):
	def updateAll(self, *args):
		self.distiller1.updateStats()
		self.distiller2.updateStats()
		self.distiller3.updateStats()
		
	def createWidgets(self):
		self.facet1 = Facet(self)
		self.facet1.grid(column=1, row=1, sticky=W)
		self.facet2 = Facet(self)
		self.facet2.grid(column=1, row=2, sticky=W)
		
		self.distiller1 = Distiller(self, '1st Distillation',
			(self.facet1, self.facet2)
		)
		self.distiller1.grid(column=1, row=3, sticky=W)
		
		self.facet3 = Facet(self)
		self.facet3.grid(column=1, row=4, sticky=W)
		self.facet4 = Facet(self)
		self.facet4.grid(column=1, row=5, sticky=W)
		
		self.distiller2 = Distiller(self, '2nd Distillation',
			(self.facet3, self.facet4)
		)
		self.distiller2.grid(column=1, row=6, sticky=W)
		
		self.facet5 = Facet(self)
		self.facet5.grid(column=1, row=7, sticky=W)
		self.facet6 = Facet(self)
		self.facet6.grid(column=1, row=8, sticky=W)
		self.facet7 = Facet(self)
		self.facet7.grid(column=1, row=9, sticky=W)
		
		self.distiller3 = Distiller(self, 'Final Distillation',
			(self.distiller1, self.distiller2, self.facet5, self.facet6, self.facet7)
		)
		self.distiller3.grid(column=1, row=10, sticky=W)
		
	def __init__(self, master):
		Frame.__init__(self, master)
		self.parent = master
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