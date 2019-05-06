import events
import characters

player1 = characters.Assault('Ramirez')
player2 = characters.Infantry('James')
player3 = characters.Gunner('Hurley')
player4 = characters.Sniper('Wu')
events.engagement(player1, player2, player3, player4, 'Sectoid', 'Floater', 'Thin Man')
