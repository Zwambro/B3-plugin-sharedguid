#
# ################################################################### #
#                                                                     #
#  sharedguid Plugin for BigBrotherBot(B3) (www.bigbrotherbot.com)    #
#  Copyright (c) 2020 Ouchekkir Abdelmouaine                          #
#                                                                     #
#  This program is free software; you can redistribute it and/or      #
#  modify it under the terms of the GNU General Public License        #
#  as published by the Free Software Foundation; either version 2     #
#  of the License, or (at your option) any later version.             #
#                                                                     #
#  This program is distributed in the hope that it will be useful,    #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the       #
#  GNU General Public License for more details.                       #
#                                                                     #
#  You should have received a copy of the GNU General Public License  #
#  along with this program; if not, write to the Free Software        #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA      #
#  02110-1301, USA.                                                   #
#                                                                     #
# ################################################################### #
#
#  Based on SharedGUIDKick script on IW4xAdmin by RaidMax
#
#  CHANGELOG:
#  08.05.2020 - v1.0 - Zwambro
#  - first release.
#





import b3
import b3.events
import b3.plugin
from b3 import functions
from collections import defaultdict
import re

__version__ = '0.1'
__author__ = 'Zwambro'


class GuidlengthPlugin(b3.plugin.Plugin):
    _adminPlugin = None
    requiresConfigFile = False
    _GenericGuid = ["-805366929435212061", "3150799945255696069", "5859032128210324569", "2908745942105435771", "-6492697076432899192", "1145760003260769995", "-7102887284306116957", "3474936520447289592", "-1168897558496584395", "8348020621355817691", "3259219574061214058", "3304388024725980231"]

    def onStartup(self):
        self._adminPlugin = self.console.getPlugin('admin')

        if not self._adminPlugin:
            self.debug('Could not find admin plugin')
            return False
        else:
            self.debug('Plugin successfully loaded')

        self.registerEvent(b3.events.EVT_CLIENT_AUTH)

    def onEvent(self, event):

        dict = self.console.game.__dict__
        game = dict['gameName']

        if event.type == b3.events.EVT_CLIENT_AUTH:
            if "cod4" in game:
                guid = event.client.guid
                for x in str(self._GenericGuid):
                    if re.match(x, guid):
                        self.debug("Client (%s) has generic GUID" %(event.client.name))
                        event.client.kick("Your GUID is generic. Delete players/guids.dat and rejoin", keyword="genericGUID")
                        return
                    return