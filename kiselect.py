# KiSelect.py

import pcbnew
import wx

class SelectDialog(pcbnew.ActionPlugin):

    def defaults( self ):
        """Support for ActionPlugins, though it doesn't work in 4.0.6 nightly and later"""
        self.name = "Select..."
        self.category = "Select"
        self.description = "Find any text on the board."
        
    def Run(self):
        _pcbnew_frame = \
            filter(lambda w: w.GetTitle().startswith('Pcbnew'), 
                   wx.GetTopLevelWindows()
            )[0]
        _pcbnew_manager = wx.aui.AuiManager.GetManager(_pcbnew_frame)

        try:
            dlg = wx.TextEntryDialog(_pcbnew_frame, "Enter text to select", defaultValue="")
            result = dlg.ShowModal()
        except Exception as e:
            self._message.SetLabel("ERROR "+str(e))
            result = None
            return
        
        if result != wx.ID_OK:
            return
        self.SearchByText(dlg.GetValue())


    def get_text_objects(self,layer=None):
        """Gets all the text objects, those on the main board and those within
           modules. If specified, the text objects are filtered to return only
           those text objects on the indicated layer."""
            
        Texts = []
        for drawing in pcbnew.GetBoard().GetDrawings():
            if isinstance(drawing,pcbnew.TEXTE_PCB):
                Texts.append(drawing)
        for module in pcbnew.GetBoard().GetModules():
            Texts.append(module.Value())
            Texts.append(module.Reference()) 
            for gi in module.GraphicalItems():
                if isinstance(gi,pcbnew.TEXTE_MODULE):
                    Texts.append(gi) 
        if layer is not None:
            Texts = filter(lambda x:x.IsOnLayer(layer),Texts)
        return Texts

    def SearchByText(self,searchtext,matchcase=False):
        if not matchcase:
            searchtext = searchtext.lower()
        for textobject in self.get_text_objects():
            text = textobject.GetShownText()
            if not matchcase:
                text = text.lower()
            if text.find(searchtext) != -1:
                textobject.SetSelected()

SelectDialog().register()