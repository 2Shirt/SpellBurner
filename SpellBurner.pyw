# Copyright 2012 Alan Mason
#
#    Spell Burner is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Spell Burner is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Spell Burner.  If not, see <http://www.gnu.org/licenses/>.
#
# Spell Burner Version 1.2

from tkinter import *
from tkinter import ttk
from math import ceil, floor, log

facetsMaBu = {
    'Element': {
        'Air': {'Actions': 4, 'Ob': 2, 'ResCost': 10,
            'Weapon': {'Power': 0, 'VA': 8, 'RangeModifier': 1},
        },
        'Anima': {'Actions': 5, 'Ob': 5, 'ResCost': 12,
            'Weapon': {'Power': 4, 'VA': 1, 'RangeModifier': -1},
        },
        'Arcana': {'Actions': 10, 'Ob': 4, 'ResCost': 13,
            'Weapon': {'Power': -1, 'VA': 1, 'RangeModifier': 3},
        },
        'Earth': {'Actions': 6, 'Ob': 1, 'ResCost': 8,
            'Weapon': {'Power': 3, 'VA': 3, 'RangeModifier': 0},
        },
        'Fire': {'Actions': 5, 'Ob': 2, 'ResCost': 10,
            'Weapon': {'Power': 2, 'VA': 2, 'RangeModifier': 0},
        },
        'Heaven': {'Actions': 8, 'Ob': 3, 'ResCost': 10,
            'Weapon': {'Power': 0, 'VA': 2, 'RangeModifier': 2},
        },
        'Water': {'Actions': 3, 'Ob': 2, 'ResCost': 9,
            'Weapon': {'Power': 1, 'VA': 3, 'RangeModifier': 0},
        },
        'White': {'Actions': 7, 'Ob': 4, 'ResCost': 11,
            'Weapon': {'Power': 5, 'VA': 4, 'RangeModifier': 0},
        },
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
        'Caster': {'Actions': 1, 'Ob': 0, 'ResCost': 0,
            'Personal': {'Length': 0, 'Range': 0},
            'Presence': {'Length': 0, 'Range': 0},
            'Sight': {'Length': 0, 'Range': 0},
        },
        'Single Target': {'Actions': 2, 'Ob': 1, 'ResCost': 2,
            'Personal': {'Length': 0, 'Range': 0},
            'Presence': {'Length': 3, 'Range': 1},
            'Sight': {'Length': 4, 'Range': 4},
        },
        'Presence': {'Actions': 3, 'Ob': 2, 'ResCost': 3,
            'Personal': {'Length': 3, 'Range': 1},
            'Presence': {'Length': 4, 'Range': 1},
            'Sight': {'Length': 4, 'Range': 6},
        },
        'Half Presence': {'Actions': 3, 'Ob': 1, 'ResCost': 2,
            'Personal': {'Length': 1, 'Range': 1},
            'Presence': {'Length': 1, 'Range': 1},
            'Sight': {'Length': 1, 'Range': 3},
        },
        'Double Presence': {'Actions': 6, 'Ob': 4, 'ResCost': 4,
            'Personal': {'Length': 4, 'Range': 2},
            'Presence': {'Length': 4, 'Range': 2},
            'Sight': {'Length': 4, 'Range': 12},
        },
        'Natural Effect': {'Actions': 4, 'Ob': 3, 'ResCost': 4,
            'Personal': {'Length': 3, 'Range': 4},
            'Presence': {'Length': 3, 'Range': 4},
            'Sight': {'Length': 4, 'Range': 8},
        },
        'Half Natural Effect': {'Actions': 3, 'Ob': 2, 'ResCost': 3,
            'Personal': {'Length': 1, 'Range': 2},
            'Presence': {'Length': 1, 'Range': 2},
            'Sight': {'Length': 2, 'Range': 4},
        },
        'Double Natural Effect': {'Actions': 8, 'Ob': 6, 'ResCost': 8,
            'Personal': {'Length': 4, 'Range': 8},
            'Presence': {'Length': 4, 'Range': 8},
            'Sight': {'Length': 4, 'Range': 16},
        },
        'Area (Paces)': {'Actions': 4, 'Ob': 2, 'ResCost': 3,
            'Personal': {'Length': 2, 'Range': 0},
            'Presence': {'Length': 3, 'Range': 1},
            'Sight': {'Length': 4, 'Range': 5},
        },
        'Area (Tens of Paces)': {'Actions': 6, 'Ob': 4, 'ResCost': 5,
            'Personal': {'Length': 4, 'Range': 1},
            'Presence': {'Length': 4, 'Range': 2},
            'Sight': {'Length': 4, 'Range': 7},
        },
        'Area (Hundreds of Paces)': {'Actions': 8, 'Ob': 6, 'ResCost': 6,
            'Personal': {'Length': 4, 'Range': 2},
            'Presence': {'Length': 4, 'Range': 3},
            'Sight': {'Length': 4, 'Range': 9},
        },
        'Area (Miles)': {'Actions': 10, 'Ob': 8, 'ResCost': 8,
            'Personal': {'Length': 4, 'Range': 4},
            'Presence': {'Length': 4, 'Range': 5},
            'Sight': {'Length': 4, 'Range': 14},
        },
        'Area (Tens of Miles)': {'Actions': 15, 'Ob': 9, 'ResCost': 9,
            'Personal': {'Length': 4, 'Range': 8},
            'Presence': {'Length': 4, 'Range': 9},
            'Sight': {'Length': 4, 'Range': 16},
        },
        'Area (Hundreds of Miles)': {'Actions': 20, 'Ob': 10, 'ResCost': 10,
            'Personal': {'Length': 4, 'Range': 12},
            'Presence': {'Length': 4, 'Range': 13},
            'Sight': {'Length': 4, 'Range': 20},
        },
    },
}

weaponLength = ['Shortest', 'Short', 'Long', 'Longer', 'Longest']

def get_facet_types():
    """Return types of Facets as as list"""
    return sorted(facetsMaBu.keys())

def get_facet_options(type):
    """Return options of facet type 'type' as as list"""
    return sorted(facetsMaBu[type].keys())

def get_facet_actions(facet, option):
    """Return actions of facet 'type', 'option' as an int()"""
    return facetsMaBu[facet][option]['Actions']

def get_facet_ob(facet, option):
    """Return obstacle of facet['type']['option'] as an int()"""
    return facetsMaBu[facet][option]['Ob']

def get_weapon_stats(elements, origins, aoes):
    """Return weapon stats, as a hash
    
    based on list(elements), list(origins), & list(aoes)"""
    weaponStats = {}
    for e in elements:
        try:
            for k in facetsMaBu['Element'][e]['Weapon']:
                try:
                    weaponStats[k] += facetsMaBu['Element'][e]['Weapon'][k]
                except KeyError:
                    weaponStats[k] = facetsMaBu['Element'][e]['Weapon'][k]
        except KeyError:
            pass
    for a in aoes:
        for o in origins:
            try:
                for k in facetsMaBu['Area of Effect'][a][o]:
                    try:
                        weaponStats[k] = max(weaponStats[k], facetsMaBu['Area of Effect'][a][o][k])
                    except KeyError:
                        weaponStats[k] = facetsMaBu['Area of Effect'][a][o][k]
            except KeyError:
                pass
    try:
        weaponStats['Length'] = weaponLength[weaponStats['Length']]
        weaponStats['Range'] += weaponStats.pop('RangeModifier')
    except KeyError:
        pass
    return weaponStats
    
def generate_range(min, max):
    """ Return a list of int()'s from min to max (inclusive)"""
    rangeList = []
    if min > max:
        # Uh....
        return [0]
    elif min == max:
        return [min]
    else:
        for i in range(min, max+1):
            rangeList.append(str(i))
        return rangeList

def round_math(x):
    """Round to the nearest int()
    
    (e.g. 1.5 -> 2.0, 2.5 -> 3.0, 2.4 -> 2.0)"""
    if (x - floor(x) >= 0.5):
        return floor(x) + 1
    else:
        return floor(x)

class Facet():
    def reset(self, *args):
        """Reset facet for a new spell"""
        self.actions.set('0')
        self.ob.set('0')
        self.option.set('')
        self.type.set(self.default)
        self.optionSelect['values'] = []
        self.update_options()
    
    def destroy(self, *args):
        """Destroy facet for a new spell"""
        try:
            self.obCombobox.destroy()
        except AttributeError:
            self.obValueLabel.destroy()
        self.typeSelect.destroy()
        self.optionSelect.destroy()
        self.obLabel.destroy()
        self.actionsLabel.destroy()
        self.actionsValueLabel.destroy()
    
    def update_options(self, *args):
        """update obCombobox based on selected facet type"""
        try:
            self.optionSelect['values'] = get_facet_options(self.type.get())
        except KeyError:
            pass
        self.actions.set('0')
        self.ob.set('0')
        self.option.set('')
        try:
            self.obCombobox.destroy()
            self.obValueLabel = ttk.Label(self.frame, textvariable=self.ob)
            self.obValueLabel.grid(column=6, row=self.row, sticky=W)
        except AttributeError:
            pass
        self.frame.update_all()
        
    def update_stats(self, *args):
        """update Actions on Ob based on selected facet type & option"""
        if self.option.get() == 'Anima':
            try:
                self.obValueLabel.destroy()
            except AttributeError:
                pass
            self.ob.set(5)
            self.obCombobox = ttk.Combobox(self.frame, textvariable=self.ob, width=2)
            self.obCombobox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            self.obCombobox.state(['readonly'])
            self.obCombobox.bind('<<ComboboxSelected>>', self.frame.update_all)
            self.obCombobox.grid(column=6, row=self.row, sticky=W)
        else:
            try:
                self.obCombobox.destroy()
            except AttributeError:
                pass
            self.ob.set(get_facet_ob(self.type.get(), self.option.get()))
            self.obValueLabel = ttk.Label(self.frame, textvariable=self.ob)
            self.obValueLabel.grid(column=6, row=self.row, sticky=W)
        self.actions.set(get_facet_actions(self.type.get(), self.option.get()))
        self.frame.update_all()
        
    def create_widgets(self):
        """Create widgets upon instantiation"""
        self.typeSelect = ttk.Combobox(self.frame, textvariable=self.type, width=18)
        self.typeSelect['values'] = get_facet_types()
        self.typeSelect.state(['readonly'])
        self.typeSelect.bind('<<ComboboxSelected>>', self.update_options)
        self.typeSelect.grid(column=1, row=self.row, columnspan=2, sticky=(W, E))
        
        self.optionSelect = ttk.Combobox(self.frame, textvariable=self.option)
        self.optionSelect.state(['readonly'])
        self.optionSelect.bind('<<ComboboxSelected>>', self.update_stats)
        self.optionSelect.grid(column=3, row=self.row, columnspan=2, sticky=(W, E))
        
        self.obLabel = ttk.Label(self.frame, text='Ob:', width=3)
        self.obLabel.grid(column=5, row=self.row, sticky=W)
        
        self.obValueLabel = ttk.Label(self.frame, textvariable=self.ob, width=6)
        self.obValueLabel.grid(column=6, row=self.row, sticky=W)
        
        self.actionsLabel = ttk.Label(self.frame, text='Actions:')
        self.actionsLabel.grid(column=7, row=self.row, sticky=W)
        
        self.actionsValueLabel = ttk.Label(self.frame, textvariable=self.actions, width=3)
        self.actionsValueLabel.grid(column=8, row=self.row, sticky=W)

    def get_actions(self):
        """return Actions as float()
        
        Will return 0.0 if facet type/option not set"""
        return float(self.actions.get())

    def get_ob(self):
        """return Ob as int()
        
        Will return 0 if facet type/option not set"""
        return float(self.ob.get())

    def get_option(self):
        """return facet option as str()
        
        Will return '' if facet type not set"""
        return str(self.option.get())

    def get_type(self):
        """return facet type as str()
        
        Will return '' if facet type not set"""
        return str(self.type.get())
        
    def __init__(self, frame, row, default=''):
        self.default = default
        self.frame = frame
        self.row = row
        self.actions = StringVar()
        self.actions.set('0')
        self.ob = StringVar()
        self.ob.set('0')
        self.option = StringVar()
        self.type = StringVar()
        self.type.set(default)
        self.create_widgets()
        try:
            self.optionSelect['values'] = get_facet_options(self.type.get())
        except KeyError:
            pass

class Distiller():
    def update_stats(self, *args):
        """Update Actions/Ob totals based on facet selections"""
        self.obTmp = 0
        self.actionsTmp = 0
        for x in self.tobedistilled:
            try:
                self.obTmp += x.get_ob()
                self.actionsTmp += x.get_actions()
            except AttributeError:
                for y in x:
                    self.obTmp += y.get_ob()
                    self.actionsTmp += y.get_actions()
        if self.final:
            self.ob.set(str(max(1,round_math(self.obTmp/2))))
            self.actions.set(str(max(1,round_math(self.actionsTmp/2))))
        else:
            self.ob.set(str(self.obTmp/2))
            self.actions.set(str(self.actionsTmp/2))
    
    def create_widgets(self):
        """Create widgets upon instantiation"""
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

    def get_actions(self):
        """return Actions as float()
        
        Will return 0.0 if facet type/option not set"""
        return float(self.actions.get())

    def get_ob(self):
        """return Ob as float()
        
        Will return 0.0 if facet type/option not set"""
        return float(self.ob.get())
    
    def __init__(self, frame, row, title, tobedistilled, final=False, *args):
        self.frame = frame
        self.row = row
        self.title = title
        self.tobedistilled = tobedistilled
        self.final = final
        self.actions = StringVar()
        self.ob = StringVar()
        self.create_widgets()
        self.update_stats()

class MajorisSigil():
    def add_sigil(self, *args):
        """Add an additional Majoris Sigil
        
        (and remove the '+' Button in the process)"""
        self.addButton.destroy()
        self.frame.add_majoris_sigil()
    
    def destroy(self, *args):
        """destroy widgets for new Spell"""
        self.addButton.destroy()
        self.toggle.destroy()
        self.obCombobox.destroy()
        self.actionsLabel.destroy()
        self.actionsEntry.destroy()
    
    def reset(self, *args):
        """Reset widgets for new Spell"""
        self.enabled.set(False)
        self.ob.set('')
        self.obCombobox['values'] = ('')
        self.obCombobox.state(['disabled'])
        self.actionsEntry.delete(0,'end')
        self.actionsEntry.state(['disabled'])
        try:
            self.addButton.destroy()
        except:
            pass
        self.addButton = ttk.Button(self.frame, text='+', command=self.add_sigil, width=3)
        self.addButton.grid(column=1, row=self.row)
    
    def toggle_sigil(self, *args):
        """Enable or Disable this Majoris Sigil"""
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
        self.frame.update_all()
    
    def validate_multiplier(self, *args):
        """Handle monkey input for Actions Multiplier"""
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
        self.frame.update_all()
        return 1
    
    def create_widgets(self):
        """Create widgets upon instantiation"""
        self.addButton = ttk.Button(self.frame, text='+', command=self.add_sigil, width=3)
        self.addButton.grid(column=1, row=self.row)
        
        self.toggle = Checkbutton(self.frame, text='Majoris', command=self.toggle_sigil,
            variable=self.enabled, onvalue=True, offvalue=False)
        self.toggle.grid(column=2, row=self.row, sticky=W)
        
        self.obCombobox = ttk.Combobox(self.frame, textvariable=self.ob, width=2)
        self.obCombobox.state(['readonly'])
        self.obCombobox['values'] = ('')
        self.obCombobox.bind('<<ComboboxSelected>>', self.frame.update_all)
        self.obCombobox.grid(column=3, row=self.row, sticky=W)
        self.obCombobox.state(['disabled'])
        
        self.actionsLabel = ttk.Label(self.frame, text='Multiplier')
        self.actionsLabel.grid(column=4, row=self.row, sticky=W)
        
        self.actionsEntry = ttk.Entry(self.frame, validate='focusout',
            validatecommand=self.validate_multiplier, width=5)
        self.actionsEntry.grid(column=5, row=self.row, sticky=W)
        self.actionsEntry.state(['disabled'])

    def get_multiplier(self):
        """return Actions Multiplier as float()
        
        Will return 0.0 if Majoris Sigil is not set"""
        if self.enabled.get():
            return float(self.actionsEntry.get())
        else:
            return 1.0

    def get_ob(self):
        """return Ob as int()
        
        Will return 0 if Majoris Sigil is not set"""
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
        self.create_widgets()

class WeaponStats():
    def update_display(self, *args):
        """Display weapon stats only if required facets are chosen"""
        if self.enabled:
            if not(self.prev):
                self.line = ttk.Separator(self.frame, orient=HORIZONTAL)
                self.line.grid(column=1, row=self.row, columnspan=8, sticky=(W, E))
                
                self.lengthValueLabel = ttk.Label(self.frame, textvariable = self.wLength)
                self.lengthValueLabel.grid(column=1, row=self.row+1, columnspan=2, sticky=(W, E))
                
                self.rangeLabel = ttk.Label(self.frame, text='Range:', justify='right')
                self.rangeLabel.grid(column=3, row=self.row+1, sticky=(W, E))
                self.rangeValueLabel = ttk.Label(self.frame, textvariable = self.wRange)
                self.rangeValueLabel.grid(column=4, row=self.row+1, sticky=(W, E))
                
                self.powerLabel = ttk.Label(self.frame, text='Power:', justify='right')
                self.powerLabel.grid(column=5, row=self.row+1, sticky=(W, E))
                self.powerValueLabel = ttk.Label(self.frame, textvariable = self.wPower)
                self.powerValueLabel.grid(column=6, row=self.row+1, sticky=(W, E))
                
                self.vaLabel = ttk.Label(self.frame, text='VA:', justify='right')
                self.vaLabel.grid(column=7, row=self.row+1, sticky=(W, E))
                self.vaValueLabel = ttk.Label(self.frame, textvariable = self.wVA)
                self.vaValueLabel.grid(column=8, row=self.row+1, sticky=(W, E))
        else:
            # hide widgets
            try:
                self.line.destroy()
                self.line.destroy()
                
                self.lengthValueLabel.destroy()
                
                self.rangeLabel.destroy()
                self.rangeValueLabel.destroy()
                
                self.powerLabel.destroy()
                self.powerValueLabel.destroy()
                
                self.vaLabel.destroy()
                self.vaValueLabel.destroy()
            except AttributeError:
                pass
    
    def update_stats(self, *args):
        """Update weapon stats
        
        based on facets: 'Element', 'Origin', and 'Area of Effect'"""
        # Initialize
        self.prev = self.enabled & True # Not link?
        self.enabled = True
        self.spell = {}
        self.tmp = {}
        for f in self.frame.facets:
            if f.get_option() == '':
                pass
            elif f.get_type() in self.spell:
                if f.get_option() in self.spell[f.get_type()]:
                    self.spell[f.get_type()][f.get_option()] += 1
                else:
                    self.spell[f.get_type()][f.get_option()] = 1
            else:
                self.spell[f.get_type()] = {}
                self.spell[f.get_type()][f.get_option()] = 1
            try:
                if self.spell[f.get_type()][f.get_option()] > 1:
                    self.frame.valid = False
            except KeyError:
                pass
        
        # Enable/Disable
        if self.enabled:
            if len(self.spell) < 5:
                self.enabled = False
                self.frame.complete = False
            else:
                if not('Destroy' in self.spell['Impetus']):
                    self.enabled = False
        
        # Update Stats
        if self.enabled:
            self.tmp = get_weapon_stats(
                list(self.spell['Element']),
                list(self.spell['Origin']),
                list(self.spell['Area of Effect'])
            )
            if len(self.tmp) == 4:
                self.wLength.set('Weapon Length:  ' + str(self.tmp['Length']))
                if self.tmp['Power'] > 0:
                    self.wPower.set('Will + ' + str(self.tmp['Power']))
                elif self.tmp['Power'] == 0:
                    self.wPower.set('Will')
                else: #self.tmp['Power'] < 0:
                    self.wPower.set('Will - ' + str(abs(self.tmp['Power'])))
                self.wRange.set(str(max(0,self.tmp['Range'])) + 'D')
                self.wVA.set(str(max(0,self.tmp['VA'] + self.frame.majObTotal - self.frame.numMin)))
            else:
                self.enabled = False
        
        # Check for Anime+Create
        #    I know this should be somewhere else in the code...
        if self.frame.complete:
            if 'Anima' in self.spell['Element']:
                if 'Create' in self.spell['Impetus']:
                    self.frame.valid = False
        
        # Update display
        self.update_display()
    
    def __init__(self, frame, row, *args):
        self.frame = frame
        self.row = row
        self.enabled = False
        self.prev = False
        self.spell = {}
        self.wDesc = StringVar()
        self.wLength = StringVar()
        self.wPower = StringVar()
        self.wRange = StringVar()
        self.wVA = StringVar()

class App(ttk.Frame):
    def add_extra_facet(self, *args):
        """Add an extra Facet (limit 10)"""
        self.facets.append(Facet(self, self.extrafacetStartRow+len(self.facets[5:])))
        
        # Update Distiller
        self.distiller3 = Distiller(self, 20, 'Final Distillation',
            (self.distiller1, self.distiller2, self.facets[4:]),
            final=True
        )
        self.configure_grid()
    
    def add_majoris_sigil(self, *args):
        """Add an additional Majoris Sigil (limit 10)"""
        if len(self.majorisSigils) < self.majorisMaxRows:
            self.majorisSigils.append(MajorisSigil(self, self.majorisStartRow + len(self.majorisSigils)))
        self.configure_grid()
    
    def configure_grid(self, *args):
        """Update window"""
        try:
            self.extraFacetButton.destroy()
        except:
            pass
        if len(self.facets[5:]) < self.extraFacetMaxRows:
            self.extraFacetButton = ttk.Button(self, text='+', command=self.add_extra_facet, width=3)
            self.extraFacetButton.grid(column=1, row=19)
            
        for child in self.winfo_children(): child.grid_configure(padx=2, pady=2)
    
    def reset(self, *args):
        """Reset all for a new Spell"""
        for f in self.facets[0:5]:
            f.reset()
        for f in self.facets[5:]:
            f.destroy()
        self.facets = self.facets[0:5]
        self.majorisSigils[0].reset()
        for m in self.majorisSigils[1:]:
            m.destroy()
        self.majorisSigils = self.majorisSigils[0:1]
        self.capValue.set(False)
        self.minorisValue.set(0)
        self.compressValue.set(0)
        self.extendValue.set(0)
        self.update_all()
        self.configure_grid()
    
    def update_all(self, *args):
        """Update all stats for this Spell"""
        ### Distillations ###
        self.distiller1.update_stats()
        self.distiller2.update_stats()
        self.distiller3.update_stats()
        
        ### Final Spell ###
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
        for m in self.majorisSigils:
            self.majObTotal += m.get_ob()
            self.majActTotal *= m.get_multiplier()
        # After Final Distillation
        self.subTotalAct = round_math(self.distiller3.get_actions())
        self.subTotalOb = round_math(self.distiller3.get_ob())
        # Before rounding
        self.preAct = max(1, self.subTotalAct)*self.majActTotal*0.5**self.numCs
        self.preEs = self.subTotalOb
        self.preEs -= self.numCap
        self.preEs -= self.numMin
        self.preEs += self.majObTotal
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
        self.complete = True
        
        if self.advanceLimits.get():
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
            #elif self.preOb == 1:
            #    self.maxEs = min(10, floor(self.preOb/2) + self.numEs)
            #    self.maxMin = min(10, self.preOb - 1 + self.numMin)
            #    self.minCs = max(0, self.numCs)
            else: # self.preOb > 1
                self.maxEs = min(10, floor((self.preEs)/2))
                self.maxMin = min(10, self.preOb - 1 + self.numMin)
                self.minCs = max(0, min(10, self.numCs - self.preOb + 1))
            
        # Set limits
        if self.numCap == 0:
            self.capValue.set(False)
        self.minorisCombobox['values'] = generate_range(self.minMin, self.maxMin)
        self.compressCombobox['values'] = generate_range(self.minCs, self.maxCs)
        self.extendCombobox['values'] = generate_range(self.minEs, self.maxEs)
        
        # Misc Checks
        if self.preOb < ceil((self.preEs)/2):
            if self.numEs > floor(self.preEs/2):
                self.valid = False
        
        # Set Stats
        if self.numCap == 0:
            self.finalOb.set(str(self.postOb) + '^')
        else:
            self.finalOb.set(self.postOb)
        self.finalActions.set(self.postAct)
        
        ### Weapon Stats ###
        self.weapon.update_stats()
        self.configure_grid()
        
        ### Warnings ###
        if self.valid:
            if self.complete:
                self.warningLabelText.set(' ')
            else:
                self.warningLabelText.set('[Incomplete]')
        else:
            self.warningLabelText.set('[HOUSE RULED]')
        
    def create_widgets(self):
        """Create widgets upon instantiation"""
        # 1st Distillation
        self.facets.append(Facet(self, 0, 'Element'))
        self.facets.append(Facet(self, 1, 'Impetus'))
        
        self.distiller1 = Distiller(self, 2, '1st Distillation',
            self.facets[0:2]
        )
        
        # 2nd Distillation
        self.facets.append(Facet(self, 5, 'Origin'))
        self.facets.append(Facet(self, 6, 'Duration'))
        
        self.distiller2 = Distiller(self, 7, '2nd Distillation',
            self.facets[2:4]
        )
        
        # 3rd Distillation
        self.facets.append(Facet(self, 10, 'Area of Effect'))
        
        self.extraFacetButton = ttk.Button(self, text='+', command=self.add_extra_facet, width=3)
        self.extraFacetButton.grid(column=1, row=19)
        
        self.distiller3 = Distiller(self, 20, 'Final Distillation',
            (self.distiller1, self.distiller2, self.facets[4:]),
            final=True
        )
        
        # Sigils
        self.sigilsLabel = ttk.Label(self, text='Sigils').grid(column=1, row=24)
        
        # Adjustments - Cap & Minoris Sigil(S)
        self.capCheckbutton = Checkbutton(self, text='Cap', command=self.update_all,
            variable=self.capValue, onvalue=True, offvalue=False)
        self.capCheckbutton.grid(column=2, row=25, sticky=W)
        
        self.minorisLabel = ttk.Label(self, text='Minoris')
        self.minorisLabel.grid(column=4, row=25, sticky=E)
        
        self.minorisCombobox = ttk.Combobox(self, textvariable=self.minorisValue, width=2)
        self.minorisCombobox.state(['readonly'])
        self.minorisCombobox['values'] = generate_range(0, 10)
        self.minorisCombobox.bind('<<ComboboxSelected>>', self.update_all)
        self.minorisCombobox.grid(column=5, row=25, sticky=W)
        
        # Adjustments - Majoris Sigil(S)
        self.majorisSigils.append(MajorisSigil(self, self.majorisStartRow))
        
        # Adjustments - Compress & Extend
        self.compressLabel = ttk.Label(self, text='Compressions')
        self.compressLabel.grid(column=2, row=36, sticky=W)
        
        self.compressCombobox = ttk.Combobox(self, textvariable=self.compressValue, width=2)
        self.compressCombobox.state(['readonly'])
        self.compressCombobox['values'] = generate_range(0, 10)
        self.compressCombobox.bind('<<ComboboxSelected>>', self.update_all)
        self.compressCombobox.grid(column=3, row=36, sticky=W)
        
        self.extendLabel = ttk.Label(self, text='Extensions')
        self.extendLabel.grid(column=4, row=36, sticky=W)
        
        self.extendCombobox = ttk.Combobox(self, textvariable=self.extendValue, width=2)
        self.extendCombobox.state(['readonly'])
        self.extendCombobox['values'] = generate_range(0, 10)
        self.extendCombobox.bind('<<ComboboxSelected>>', self.update_all)
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
        
        # Weapon Stats
        self.weapon = WeaponStats(self, 39)
        
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame = master

        # Menu Bar
        self.advanceLimits = BooleanVar()
        self.advanceLimits.set(True)
        menubar = Menu(self.frame)
        self.frame['menu'] = menubar
        menu_file = Menu(menubar)
        menu_settings = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_settings, label='Settings')
        menu_file.add_command(label='New', command=self.reset)
        #menu_file.add_command(label='Open...')
        menu_file.add_command(label='Close', command=quit)
        menu_settings.add_checkbutton(label='Advanced Limiting',
            variable=self.advanceLimits, onvalue=True, offvalue=False,
            command=self.update_all
        )

        self.capValue = BooleanVar()
        self.capValue.set(False)
        self.compressValue = StringVar()
        self.compressValue.set(0)
        self.extendValue = StringVar()
        self.extendValue.set(0)
        self.minorisValue = StringVar()
        self.minorisValue.set(0)
        self.majorisStartRow = 26
        self.majorisMaxRows = 10
        self.extrafacetStartRow = 11
        self.extraFacetMaxRows = 9
        self.facets = []
        self.finalOb = StringVar()
        self.finalObValue = 1
        self.finalActions = StringVar()
        self.finalActionsValue = 1
        self.majorisSigils = []
        self.create_widgets()
        self.update_all()
        self.configure_grid()

root = Tk()
root.title('Spell Burner')
if root.tk.call('tk', 'windowingsystem') == 'win32':
    # Enable icon only under windows
    # ToDo: fix for Linux/MacOS X
    try:
        root.iconbitmap("SpellBurner.ico")
    except TclError:
        pass
#root.resizable(0, 0)                       # disable window resizing
root.resizable(width=FALSE, height=FALSE)   # disable window resizing
root.option_add('*tearOff', FALSE)

app = App(root)
app.grid(column=0, row=0, sticky=(N, W, E, S))
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

root.mainloop()
