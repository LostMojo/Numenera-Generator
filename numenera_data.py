
# Change Abilities so that pool costs are in the description rather than the Key?

type_template = {
    "Base Stats": [5, 5, 5],
    "Starting Edge": [0, 0, 0],
    "Weapon Proficiencies": [],
    "Class Skills": [],
    "Class Inabilities": [],
    "Class Intrusions": {},
    "Cypher Limit": 2,
    "Starting Equipment": [],
    "Default Cyphers": [],
    "Default Oddity": [],
    "Community Bonus": [],
    "Connection": "",
    "Tiers": {
        '1': {},
        '2': {},
        '3': {},
        '4': {},
        '5': {},
        '6': {}
    }
}

types = {
    "Glaive": {
        "Base Stats": [11, 10, 7],
        "Starting Edge": [1, 1, 0],
        "Weapon Proficiencies": ["Light", "Medium", "Heavy"],
        "Class Skills": ["CHOICE:Physical Skill"],
        "Abilities": {"Combat Prowess":
                           "You add +1 damage to one type of attack of your choice: melee attacks or ranged "
                           "attacks. Enabler.",
                           "Trained in Armor":
                           "You can wear armor for long periods of time without tiring and can compensate for "
                           "slowed reactions from wearing armor. You reduce the Speed Effort cost for wearing "
                           "armor by 1. Enabler.",},
        "Cypher Limit": 2,
        "Class Intrusions": {"Perfect Setup":
                             "You’re fighting at least three foes and each one is standing in exactly the right "
                             "spot for you to use a move you trained in long ago, allowing you to attack all three "
                             "as a single action. Make a separate attack roll for each foe. You remain limited by "
                             "the amount of Effort you can apply on one action.",
                             "Old Friend":
                             "A comrade in arms from your past shows up unexpectedly and provides aid in whatever "
                             "you’re doing. They are on a mission of their own and can’t stay longer than it takes "
                             "to help out, chat a while after, and perhaps share a quick meal.",
                             "Weapon Break":
                             "Your foe’s weapon has a weak spot and in the course of the combat quickly becomes "
                             "damaged and moves two steps down the object damage track."
                             },
        "Starting Equipment": ["Clothing", "Weapon 1", "Weapon 2 or Shield", "Light or Medium Armor", "2 Cyphers",
                               "1 Oddity", "If a ranged weapon, 12 Ammo of its type", "5 Shins", ],
        "Default Cyphers": ["Destiny Nodule", "Rejuvinator"],
        "Default Oddity": "Shifting Blob of Clay",
        "Community Bonus": "",
        "Connection": "",
        "Tiers": {
            '1': {"Combat Prowess": "You add +1 damage to one type of attack of your choice: melee attacks or "
                                    "ranged attacks. Enabler.",
                  "Trained in Armor":
                      "You can wear armor for long periods of time without tiring and can compensate for slowed "
                      "reactions from wearing armor. You reduce the Speed Effort cost for wearing armor by 1. Enabler.",
                  "CHOOSE2": {
                      "Aggression":
                        "(2 Might Points) "
                        "You focus on making attacks to such an extent that you leave yourself vulnerable to your "
                        "opponents. While this ability is active, you gain an asset on your melee attacks, and your "
                        "Speed defense rolls against melee and ranged attacks are hindered. This effect lasts for as "
                        "long as you wish, but it ends if no combat is taking place within range of your senses. "
                        "Enabler.",
                      "Fleet of Foot":
                        "(1+ Speed points)"
                        "You can move a short distance as part of another action. You can move a long distance as your "
                        "entire action for a turn. If you apply a level of Effort to this ability, you can move a long "
                        "distance and make an attack as your entire action for a turn, but the attack is hindered. "
                        "Enabler.",
                      "Impressive Display":
                        "(2 Might points) "
                        "You perform a feat of strength, speed, or combat, impressing those nearby. For the next "
                        "minute you gain an asset in all interaction tasks with people who saw you use this ability."
                        " Action.",
                      "Misdirect":
                        "(3 Speed points)"
                        "When an opponent misses you, you can redirect their attack to another target (a creature or "
                        "object) of your choosing that’s within immediate range of you. Make an unmodified attack roll "
                        "against the new target (do not use any of your or the opponent’s modifiers to the attack roll,"
                        " but you can apply Effort for accuracy). If the attack hits, the target takes damage from your"
                        " opponent’s attack. Enabler.",
                      "No Need for Weapons":
                        "When you make an unarmed attack (such as a punch or kick), it counts as a medium weapon "
                        "instead of a light weapon. Enabler.",
                      "Trained Without Armor": "You are trained in Speed defense actions when not wearing armor."
                                               " Enabler."
            }},
            '2': {"Skill With Attacks":
                    "Choose one type of attack inwhich you are not already trained: light bashing, light bladed, "
                    "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or "
                    "heavy ranged. You are trained in attacks using that type of weapon. Enabler.",
                  "CHOOSE1": {
                     "Crushing Blow":
                         "(2 Might points)"
                         "When you use a bashing or bladed weapon in both hands and apply Effort on the attack, you "
                         "get a free level of Effort on the damage. (If fighting unarmed, this attack is made with "
                         "both fists or both feet together.) Action.",
                     "Hemorrhage":
                         "(2+ Might points) "
                         "You make a powerful and precise strike that inflicts additional damage later. On your next "
                         "turn, the target of this attack takes an additional 3 points of damage (this ignores Armor). "
                         "The target can prevent this additional damage by making a recovery roll, using any ability "
                         "that heals it, or using its action to attend to the injury. In addition to the normal options"
                         " for using Effort, you can choose to use Effort to increase this duration by one round. "
                         "Action.",
                     "Reload":
                         "(1 Speed point) "
                         "When using a weapon that normally requires an action to reload, such as a heavy crossbow, "
                         "you can reload and fire (or fire and reload) in the same action. Enabler.",
                     "Skill With Defense":
                         "Choose one type of defense task in which you are not already trained: Might, Speed, or "
                         "Intellect. You are trained in defense tasks of that type. Unlike most fighting moves, you "
                         "can select this move up to three times. Each time you select it, you must choose a different "
                         "type of defense task. Enabler.",
                     "Successive Attack":
                         "(2 Speed points)"
                         "If you take down a foe, you can immediately make another attack on that same turn against a "
                         "new foe within your reach. The second attack is part of the same action. You can use this "
                         "fighting move with melee attacks and ranged attacks. Enabler.",
                 }},
            '3': {"Expert Cypher Use": "You can bear three cyphers at a time.",
                  "Skill With Attacks":
                      "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                      "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or "
                      "heavy ranged. You are trained in attacks using that type of weapon. Enabler.",
                  "CHOOSE1": {
                     "Energy Resistance":
                         "Choose a discrete type of energy that you have experience with (such as heat, sonic, "
                         "electricity, and so on). You gain +5 to Armor against damage from that type of energy. You "
                         "must be familiar with the type of energy; for example, if you have no experience with a "
                         "certain kind of extradimensional energy, you can’t protect against it. Unlike most fighting "
                         "moves, you can select this more than once. Each time you select it, you must choose a "
                         "different kind of energy. Enabler.",
                     "Lunge":
                         "(2 Might points) This move requires you to extend yourself for a powerful stab or smash. "
                         "The awkward lunge "
                         "hinders the attack roll. If your attack is successful, it inflicts 4 additional points of "
                         "damage. Action.",
                     "Obstacle Running":
                         "(3 Speed points)"
                         "For the next minute, you can ignore obstacles that slow your movement, allowing you to travel"
                         " at normal speed through areas with rubble, fences, tables, and similar objects that you "
                         "would have to climb over or move around. This movement might include sliding on a railing, "
                         "briefly running along a wall, or even stepping on a creature to boost yourself over "
                         "something. If an obstacle would normally require a Might or Speed task to overcome, such as "
                         "swinging on a rope, balancing on a rope, or jumping over a hole, you are trained at that "
                         "task. Enabler.",
                     "Slice":
                         "(2 Speed points) "
                         "This is a quick attack with a bladed or pointed weapon that is hard to defend against. You "
                         "are trained in this task. If the attack is successful, it deals 1 less point of damage than "
                         "normal. Action.",
                     "Specialized in Armor":
                         "The cost reduction from your Trained in Armor ability improves. You now reduce the Speed "
                         "Effort cost for wearing armor by an additional 1. Enabler.",
                     "Spray":
                         "(2 Speed points)"
                         "If a weapon has the ability to fire rapid shots without reloading (usually called a rapid-"
                         "fire weapon, such as a crank crossbow), you can spray multiple shots around your target to "
                         "increase the chance of hitting. This move uses 1d6 + 1 rounds of ammo (or all the ammo in "
                         "the weapon, if it has less than the number rolled). You are trained in making this attack. "
                         "If the attack is successful, it deals 1 less point of damage than normal. Action.",
                     "Trick Shot":
                         "(2 Speed points) "
                         "As part of the same action, you make a ranged attack against two targets that are within "
                         "immediate range of each other. Make a separate attack roll against each target. The attack "
                         "rolls are hindered. Action.",
                     "Vigilance":
                         "(2 Intellect points) "
                         "You take a cautious approach to combat, focusing more on protecting yourself than on hurting "
                         "your opponents. While this ability is active, you gain an asset on Speed defense rolls "
                         "against melee and ranged attacks, and your melee and ranged attacks are hindered. This "
                         "effect lasts for as long as you wish, but it ends if no combat is taking place within range "
                         "of your senses. Action to initiate.",
                 }},
            '4': {"Skill With Attacks":
                     "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                     "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or "
                     "heavy ranged. You are trained in attacks using that type of weapon. Enabler.",
                  "CHOOSE1": {
                     "Amazing Effort":
                         "When you apply at least one level of Effort to a non-combat task, you get a free level of "
                         "Effort on that task. When you choose this fighting move, decide if this ability applies to "
                         "Might Effort or Speed Effort. Enabler.",
                     "Capable Warrior": "Your attacks deal 1 additional point of damage. Enabler.",
                     "Experienced Defender": "When wearing armor, you gain +1 to Armor. Enabler.",
                     "Feint":
                         "(2 Speed points) "
                         "If you spend one action creating a misdirection or diversion, in the next round you can take "
                         "advantage of your opponent’s lowered defenses. Make a melee attack roll against that "
                         "opponent. You gain an asset on this attack. If your attack is successful, it inflicts 4 "
                         "additional points of damage. Action.",
                     "Minor to Major":
                         "You treat rolls of natural 19 as rolls of natural 20 for Might attack rolls or Speed attack "
                         "rolls (your choice when you gain this ability). This allows you to gain a major effect on a "
                         "natural 19 or 20. Enabler.",
                     "Snipe":
                         "(2 Speed points) If you spend one action aiming, in the next round you can make a precise "
                         "ranged attack. You "
                         "are trained in this task. If your attack is successful, it inflicts 4 additional points of "
                         "damage. Action.",
                 }},
            '5': {"Adept Cypher Use": "You can bear four cyphers at a time.",
                  "Mastery With Attacks":
                     "Choose one type of attack in which you are trained: light bashing, light bladed, light ranged, "
                     "medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or heavy ranged. You "
                     "are specialized in attacks using that type of weapon.Enabler.(In place of this ability, you may "
                     "instead select Skill With Attacks to become trained in one type of attack.)",
                  "CHOOSE1": {
                    "Mastery in Armor":
                        "The cost reduction from your Trained in Armor ability improves. You now reduce the Speed "
                        "Effort cost for wearing armor by an additional 1. Enabler.",
                    "Arc Spray":
                        "If a weapon has the ability to fire rapid shots without reloading (usually called a rapid-fire"
                        " weapon, such as a crank crossbow), you can fire your weapon at up to three targets (all next "
                        "to one another) at once. Make a separate attack roll against each target. Each attack is "
                        "hindered. Action.",
                    "Battlefield Tactician":
                        "(2+ Intellect points) You scrutinize your surroundings, learning whatever facts the GM feels"
                        " are pertinent about "
                        "attacking, defending, maneuvering, and dealing with environmental hazards within a short "
                        "distance. For example, you might notice a pile of rubble you can stand on for an advantage in "
                        "melee, a sheltered corner to help protect against enemy attacks, a less-slippery part of a "
                        "frozen lake, or a place where the poison gas is thinner than elsewhere. If you (or someone "
                        "you tell) move to that location, you (or the person told) gain an asset on tasks related to "
                        "that optimal position (such as attack rolls from the high ground, Speed defense rolls from the"
                        " sheltered corner, balance rolls on the frozen lake, or Might defense rolls against the "
                        "poisonous cloud). Instead of gaining an advantageous location, you might learn a "
                        "disadvantageous location that you could use against your enemies, such as maneuvering them "
                        "into an awkward corner that hinders their melee attacks or a weak spot on the frozen lake that"
                        " will break if they stand on it. You can apply Effort to learn one additional good or bad "
                        "location within range (one location per level of Effort), increase the range of this ability "
                        "(another short distance per level of Effort), or both. Enabler.",
                    "Jump Attack":
                        "(5 Might points) You attempt a difficulty 4 Might roll to jump high into the air as part of "
                        "your melee attack "
                        "action. If you succeed at the jump and your attack hits, you inflict 3 additional points of "
                        "damage and knock the foe prone. If you fail at the jump, you still make your normal attack "
                        "roll, but you don’t inflict the extra damage or knock down the opponent if you hit. In "
                        "addition to the normal options for using Effort, you can choose to use Effort to enhance "
                        "your jump; each level of Effort used in this way adds +2 feet to the height and +1 damage to "
                        "the attack. Action.",
                    "Mastery With Defense":
                        "Choose one type of defense task in which you are trained: Might, Speed, or Intellect. You are "
                        "specialized in defense tasks of that type. Unlike most fighting moves, you can select this "
                        "move up to three times. Each time you select it, you must choose a different type of defense "
                        "task. Enabler.",
                    "Parry":
                        "(5 Speed points) You can deflect incoming attacks quickly. When you activate this move, "
                        "for the next ten rounds you ease all Speed defense rolls. Enabler.",
                 }},
            '6': {"Mastery With Attacks":
                     "Choose one type of attack in which you are trained: light bashing, light bladed, light ranged, "
                     "medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or heavy ranged. You "
                     "are specialized in attacks using that type of weapon. Enabler. (In place of this ability, you "
                     "may instead select Skill With Attacks to become trained in one type of attack.)",
                  "CHOOSE1": {
                     "Again and Again":
                         "(8 Speed points) You can take an additional action in a round in which you have already "
                         "acted. Enabler.",
                     "Finishing Blow":
                         "(5 Might points) If your foe is prone, stunned, or somehow helpless or incapacitated when "
                         "you strike, you "
                         "inflict 7 additional points of damage on a successful hit. Enabler.",
                     "Slayer":
                         "(3 Might points) When you successfully strike an NPC or creature of level 5 or lower, make "
                         "another roll "
                         "(using whichever stat you used to attack). If you succeed on the second roll, you kill the "
                         "target outright. If you use this fighting move against a PC of any tier and you succeed on "
                         "the second roll, the character moves down one step on the damage track. Enabler.",
                     "Spin Attack":
                         "(5 Speed points) You stand still and make attacks against up to five foes, all as part of "
                         "the same action in "
                         "one round. All of the attacks have to be the same sort of attack (melee or ranged). Make a "
                         "separate attack roll for each foe. You remain limited by the amount of Effort you can apply "
                         "on one action. Anything that modifies your attack or damage applies to all of these attacks. "
                         "In addition to the normal options for using Effort, you can choose to use Effort to increase "
                         "the number of foes you can attack with this ability (one additional foe per level of Effort "
                         "used in this way). Action.",
                 }}
        }
    },
    "Nano": {
        "Base Stats": [7, 9, 12],
        "Starting Edge": [0, 0, 1],
        "Weapon Proficiencies": ["Light"],
        "Class Skills": ["Understanding Numenera"],
        "Cypher Limit": 3,
        "Starting Equipment": ["Clothing", "Weapon", "Book About The Numenera", "3 Cyphers", "1 Oddity"],
        "Default Cyphers": ["Gravity Nullifying Spray", "Telepathy Implant", "Teleporter"],
        "Default Oddity": "Infinity Thermos",
        "Community Bonus": "",
        "Tiers": {
            '1': {"CHOOSE2": {
                "Hedge Magic":
                    "(1 Intellect point) You can perform small tricks: temporarily change the color or basic "
                    "appearance of a small object, "
                    "cause small objects to float through the air, clean a small area, mend a broken object, prepare "
                    "(but not create) food, and so on. You can’t use Hedge Magic to harm another creature or object. "
                    "Action.",
                "Onslaught":
                    "(1 Intellect point) You attack a foe using energies that assail either their physical form or "
                    "their mind. In either "
                    "case, you must be able to see your target. If the attack is physical, you emit a short-range ray "
                    "of force that inflicts 4 points of damage. If the attack is mental, you focus your mental energy "
                    "to blast the thought processes of another creature within short range. This mindslice inflicts 2 "
                    "points of Intellect damage (and thus ignores Armor). Some creatures without minds (such as "
                    "automatons) might be immune to your mindslice. Action.",
                "Push":
                    "(2 Intellect points) You push a creature or object an immediate distance in any direction you "
                    "wish. You must be able "
                    "to see the target, which must be your size or smaller, must not be affixed to anything, and must "
                    "be within short range. The push is quick, and the force is too crude to be manipulated. For "
                    "example, you can’t use this esotery to pull a lever or even close a door. Action.",
                "Scan":
                    "(2 Intellect points) You scan an area equal in size to a 10-foot (3 m) cube, including all "
                    "objects or creatures within "
                    "that area. The area must be within short range. Scanning a creature or object always reveals its "
                    "level (a measure of how powerful, dangerous, or difficult it is). You also learn whatever facts "
                    "the GM feels are pertinent about the matter and energy in that area. For example, you might learn "
                    "that the wooden box contains a device of metal and synth. You might learn that the glass cylinder "
                    "is full of poisonous gas, and that its metal stand has an electrical field running through it that"
                    " connects to a metal mesh in the floor. You might learn that the creature standing before you is a"
                    " mammal with a small brain. However, this esotery doesn’t tell you what the information means. "
                    "Thus, in the first example, you don’t know what the metal and synth device does. In the second, "
                    "you don’t know if stepping on the floor causes the cylinder to release the gas. In the third, you "
                    "might suspect that the creature is not very intelligent, but scans, like looks, can be deceiving. "
                    "Many materials and energy fields prevent or resist scanning. Action.",
                "Ward":
                    "You have a shield of energy around you at all times that helps deflect attacks. You gain +1 to "
                    "Armor. Enabler.",
            }},
            '2': {"CHOOSE1": {
                "Adaptation":
                    "(2+ Intellect points) You adapt to a hostile environment for 28 hours. As a result, you can "
                    "breathe safely, the "
                    "temperature doesn't kill you (though it might be extremely uncomfortable or debilitating), "
                    "crushing gravity doesn’t incapacitate or harm you (though, again, you might be seriously "
                    "hindered), and so on. In extreme environments, the GM might increase the cost of activating this "
                    "esotery to a maximum cost of 10 Intellect points. Roughly speaking, the cost should equal the "
                    "amount of damage you would sustain in a given round. For example, if you enter a hostile "
                    "environment that would normally deal 6 points of damage per round, using Adaptation to avoid that "
                    "damage costs 6 points. You can protect other creatures in addition to yourself, but each "
                    "additional creature costs you the same number of Intellect points as it costs to protect you. "
                    "Thus, if it costs 6 points to protect yourself, it costs 12 more to protect two other people. "
                    "This esotery never protects against quick, instantaneous threats, like an attack with a weapon or "
                    "a sudden explosion of fire. Action to initiate.",
                "Flash":
                    "(4 Intellect points) You create an explosion of energy at a point within close range, affecting "
                    "an area up to immediate range from that point. You must be able to see the location where you "
                    "intend to center the explosion. The blast inflicts 2 points of damage to all creatures or objects "
                    "within the area. "
                    "Because this is an area attack, adding Effort to increase your damage works differently than it "
                    "does for single- target attacks. If you apply a level of Effort to increase the damage, add 2 "
                    "points of damage for each target, and even if you fail your attack roll, all targets in the area "
                    "still take 1 point of damage. Action.",
                "Hover":
                    "(2 Intellect points) You float slowly into the air. If you concentrate, you can control your "
                    "movement to remain "
                    "motionless in the air or float up to a short distance as your action; otherwise, you drift with "
                    "the wind or with any momentum you have gained. This effect lasts for up to ten minutes. Action to "
                    "initiate.",
                "Mind Reading":
                    "(4 Intellect points) You can read the surface thoughts of a creature within short range of you,"
                    " even if the target "
                    "doesn't want you to. You must be able to see the target. Once you have established contact, you "
                    "can read the target’s thoughts for up to one minute. If you or the target move out of range, the "
                    "connection is broken. Action to initiate.",
                "Stasis":
                    "(3 Intellect points) You surround a foe of your size or smaller with scintillating energy, keeping"
                    " it from moving or acting for one minute, as if frozen solid. You must be able to see the target, "
                    "and it must be within short range. While in stasis, the target is impervious to harm, cannot be "
                    "moved, and is immune to all effects. Action.",
            }},
            '3': {"Adept Cypher Use": "You can bear four cyphers at a time.",
                  "CHOOSE1": {
                     "Barrier":
                         "(3+ Intellect points) You create an opaque, stationary barrier of solid energy within "
                         "immediate range. The barrier is 10 feet by 10 feet (3 m by 3 m) and of negligible thickness. "
                         "It is a level 2 barrier and lasts for ten minutes. It can be placed anywhere it fits, whether"
                         " against a solid object (including the ground) or floating in the air. Each level of Effort "
                         "you apply strengthens the barrier by one level. For example, applying two levels of Effort "
                         "creates a level 4 barrier. Action.",
                     "Countermeasures":
                         "(4 Intellect points) You immediately end one ongoing numenera effect (such as an effect "
                         "created by an esotery) within immediate range. Alternatively, you can use this as a defense "
                         "action to cancel any incoming esotery targeted at you, or you can cancel any numenera "
                         "device or the effect of any numenera device for 1d6 rounds. You must touch the effect or "
                         "device to cancel it. Action.",
                     "Energy Protection":
                         "(3+ Intellect points) Choose a discrete type of energy that you have experience with (such "
                         "as heat, sonic, electricity, and so on). You gain +10 to Armor against damage from that type "
                         "of energy for ten minutes. Alternatively, you gain +1 to Armor against damage from that "
                         "energy for 28 hours. You must be familiar with the type of energy; for example, if you have "
                         "no experience with a certain kind of extradimensional energy, you can’t protect against it. "
                         "In addition to the normal options for using Effort, you can choose to use Effort to protect "
                         "more targets; each level of Effort used in this way affects up to two additional targets. "
                         "You must touch additional targets to protect them. Action to initiate.",
                     "Sensor":
                         "(4 Intellect points) You create an immobile, invisible sensor within immediate range that "
                         "lasts for 28 hours. At any time during that duration, you can concentrate to see, hear, and "
                         "smell through the sensor, no matter how far you move from it. The sensor doesn’t grant you "
                         "sensory capabilities beyond the norm. Action to create; action to check.",
                     "Targeting Eye":
                         "You are trained in any physical ranged attack that is an esotery or comes from a numenera "
                         "device. For example, you are trained when using an Onslaught force blast because it’s a "
                         "physical attack, but not when using an Onslaught mindslice because it’s a mental attack. "
                         "Enabler.",
                 }},
            '4': {"CHOOSE1":{
                "Invisibility":
                    "(4 Intellect points) You become invisible for ten minutes. While invisible, you are specialized in"
                    " stealth and Speed defense tasks. This effect ends if you do something to reveal your presence or "
                    "position—attacking, performing an esotery, using an ability, moving a large object, and so on. If "
                    "this occurs, you can regain the remaining invisibility effect by taking an action to focus on "
                    "hiding your position. Action to initiate or reinitiate.",
                "Mind Control":
                    "(6+ Intellect points) You control the actions of another creature you touch. This effect lasts "
                    "for one minute. The target must be level 2 or lower. Once you have established control, you "
                    "maintain mental contact with the target and sense what it senses. You can allow it to act freely "
                    "or override its control on a case-by-case basis. In addition to the normal options for using "
                    "Effort, you can choose to use Effort to increase the maximum level of the target or increase the "
                    "duration by one minute. Thus, to control the mind of a level 5 target (three levels above the "
                    "normal limit) or control a target for four minutes (three levels above the normal duration), you "
                    "must apply three levels of Effort. Smart Nanos use the Scan esotery on a creature to learn its "
                    "level before trying to control its mind. When the Mind Control esotery ends, the creature "
                    "doesn't remember being controlled or anything it did while under your command. "
                    "Action to initiate.",
                "Regeneration":
                    "(6 Intellect points) You restore points to a target’s Might or Speed Pool in one of two ways: "
                    "either the chosen Pool regains up to 6 points, or it is restored to a total value of 12. You "
                    "make this decision when you initiate this esotery. Points are regenerated at a rate of 1 point "
                    "each round. You must maintain contact with the target the whole time. In no case can this raise "
                    "a Pool higher than its maximum. Action.",
                "Reshape":
                    "(5 Intellect points) You reshape matter within short range in an area no larger than a 5-foot "
                    "(1.5 m) cube. If you use only one action on this esotery, the changes you make are crude at best. "
                    "If you spend at least ten minutes and succeed at an appropriate crafting task (which is hindered, "
                    "due to the circumstances), you can make complex changes to the material. You can’t change the "
                    "nature of the material, only its shape. Thus, you can make a hole in a wall or floor, or you can "
                    "seal one up. You can fashion a rudimentary sword from a large piece of iron. You can break or "
                    "repair a chain. With multiple uses of this esotery, you could bring about large changes, making "
                    "a bridge, a wall, or a similar structure. Action.",
                "Slay":
                    "(6 Intellect points) You gather disrupting energy in your fingertip and touch a creature. If the "
                    "target is an NPC or a creature of level 3 or lower, it dies. If the target is a PC of any tier, "
                    "they move down one step on the damage track. Action.",
            }},
            '5': {"Master Cypher Use": "You can bear five cyphers at a time.",
                  "CHOOSE1": {
                     "Absorb Energy ":
                         "(7 Intellect points) You touch an object and absorb its energy. If you touch a cypher, you "
                         "render it useless. If you touch an artifact, roll for the artifact’s depletion. If you touch "
                         "another kind of powered machine or device, the GM determines whether its power is fully "
                         "drained. In any case, you absorb energy from the object touched and regain 1d10 Intellect "
                         "points. If this would give you more Intellect than your Pool’s maximum, the extra points are "
                         "lost, and you must make a Might defense roll. The difficulty of the roll is equal to the "
                         "number of points over your maximum you absorbed. If you fail the roll, you take 5 points of "
                         "damage and are unable to act for one round. You can use this esotery as a defense action "
                         "when you’re the target of an incoming esotery. Doing so cancels the incoming esotery, and "
                         "you absorb the energy as if it were a device. Action.",
                     "Dust to Dust":
                         "(7 Intellect points) You disintegrate one object that is smaller than you and whose level is "
                         "less than or equal to your tier. You must touch the object to affect it. If the GM feels it "
                         "appropriate to the circumstances, you can disintegrate a portion of an object (the total "
                         "volume of which is smaller than you) rather than the entire thing. Action.",
                     "Knowing the Unknown":
                         "(6 Intellect points) Tapping into the datasphere, you can ask the GM one question and get a "
                         "general answer. The GM assigns a level to the question, so the more obscure the answer, the "
                         "more difficult the task. Generally, knowledge that you could find by looking somewhere other "
                         "than your current location is level 1, and obscure  knowledge of the past is level 7. "
                         "Gaining knowledge of the future is impossible. Action.",
                     "Teleportation":
                         "(6+ Intellect points) You instantaneously transmit yourself to any location that you have "
                         "seen or been to, no matter the distance, as long as it is on Earth (or whatever world you’re "
                         "currently on). In addition to the normal options for using Effort, you can choose to use "
                         "Effort to bring other people with you; each level of Effort used in this way affects up to "
                         "three additional targets. You must touch any additional targets. Action.",
                     "True Senses":
                         "You can see in complete darkness up to 50 feet (15 m) as if it were dim light. You recognize "
                         "holograms, disguises, optical illusions, sound mimicry, and other such tricks (for all "
                         "senses) for what they are. Enabler."
                 }},
            '6': {"CHOOSE1": {
                "Control Weather":
                    "(10 Intellect points) You change the weather in your general region. If performed indoors, this "
                    "esotery creates only minor weather effects, such as mist, mild temperature changes, and so on. "
                    "If performed outside, you can create rain, fog, snow, wind, or any other kind of normal (not "
                    "overly severe) weather. The change lasts for a natural length of time, so a storm might last for "
                    "an hour, fog for two or three hours, and snow for a few hours (or for ten minutes if it’s out of "
                    "season). For the first ten minutes after activating this esotery, you can create more dramatic "
                    "and specific effects, such as lightning strikes, giant hailstones, twisters, hurricane force "
                    "winds, and so on. These effects must occur within 1,000 feet (300 m) of your location. You must "
                    "spend your turn concentrating to create an effect or to maintain it in a new round. These effects "
                    "inflict 6 points of damage each round. Action.",
                "Move Mountains":
                    "(9 Intellect points) You exert a tremendous amount of physical force within 250 feet (75 m) of "
                    "you. You can push up to 10 tons (9 t) of material up to 50 feet (15 m). This force can collapse "
                    "buildings, redirect small rivers, or perform other dramatic effects. Action.",
                "Traverse the Worlds":
                    "(8+ Intellect points) You instantaneously transmit yourself to another planet, dimension, plane, "
                    "or level of reality. You must know that the destination exists; the GM will decide if you have "
                    "enough information to confirm its existence and the level of difficulty to reach the destination. "
                    "In addition to the normal options for using Effort, you can choose to use Effort to bring other "
                    "people with you; each level of Effort used in this way affects up to three additional targets. "
                    "You must touch any additional targets. Action.",
                "Usurp Cypher":
                    "Choose one cypher that you carry. The cypher must have an effect that is not instantaneous. You "
                    "destroy the cypher and gain its power, which functions for you continuously. You can choose a "
                    "cypher when you gain this ability, or you can wait and make the choice later. However, once you "
                    "usurp a cypher’s power, you cannot later switch to a different cypher—the esotery works only "
                    "once. Action to initiate.",
            }}
        }
    },
    "Jack": {
        "Base Stats": [10, 10, 10],
        "Starting Edge": "CHOICE",         #Choice: Add one edge to chosen pool
        "Weapon Proficiencies": ["Light", "Medium"],
        "Class Skills": ["CHOICE:Any Skill", "FLEX SKILL"],
        "Class Intrusions": {
            "Familiar Insight":
                "You know this person (or heard about them somewhere) well enough to give insight about their motives "
                "or intentions and how best to convince them to see things your way. You know the right words, "
                "posturing, inflection, amount of emotional manipulation, or even what sort of joke or agreeable "
                "complaint might sway them. This can convince a neutral person to take your side, or a hostile one to "
                "hear you out for a little while longer.",
            "Inspirational Recall":
                "You recall an important detail from a previous encounter (perhaps something you don’t even remember "
                "noticing at the time) that suggests a successful course of action for your current situation. This "
                "might be recognizing a password hidden in an innocuous code or riddle, realizing you saw a suspicious "
                "individual near a crime scene, overhearing an important conversation between two NPCs, or "
                "understanding that an NPC’s subtle glance or gesture had additional connotations indicating what you "
                "should do.",
            "Lucky Break":
                "Something unexpected happens that is to your advantage. A rope your opponent is hanging from might "
                "snap, the person you’re debating in front of an influential Aeon Priest might trip or forget what "
                "they were going to say, or something that was supposed to last only a round or two lasts a little "
                "while longer.",
        },
        "Cypher Limit": 2,
        "Starting Equipment": ["Clothing", "Weapon 1", "Weapon 2", "light armor", "an explorer’s pack",
                               "a pack of light tools", "Cypher 1", "Cypher 2", "Oddity", "8 shins"],
        "Default Cyphers": ["Machine Control Implant", "Visage Changer"],
        "Default Oddity": "Small Square Stasis Cage",
        "Community Bonus": "",
        "Tiers": {
            '1': {"Flex Skill":
                    "At the beginning of each day, choose one task (other than attacks or defense) on which you will "
                    "concentrate. For the rest of that day, you’re trained in that task. You can’t use this ability "
                    "with a skill you’re already trained in to become specialized.",
                  "CHOOSE2": {
                    "Trained in Armor":
                        "You can wear armor for long periods of time without tiring and can compensate for slowed "
                        "reactions from wearing armor. You can wear any kind of armor. You reduce the Speed Effort "
                        "cost for wearing armor by 1. Enabler.",
                    "Create Deadly Poison":
                        "(3+ Intellect points) You create one dose of a level 2 poison that inflicts 5 points of "
                        "damage. You can apply this poison to a weapon, food, or drink as part of the action of "
                        "creating it. In addition to the normal options for using Effort, you can choose to use Effort "
                        "to increase the level of the poison; each level of Effort used in this way increases the "
                        "poison level by 1. If unused, the poison loses its potency after one hour. Action.",
                    "Critter Companion":
                        "A level 1 creature accompanies you and follows your instructions. This creature is no larger "
                        "than a large cat (about 20 pounds, or 9 kg) and is normally some sort of domesticated species."
                        " You and the GM must work out the details of your creature, and you’ll probably make rolls for"
                        " it in combat or when it takes actions. The critter companion acts on your turn. As a level 1 "
                        "creature, it has a target number of 3 and a 3 health, and it inflicts 1 point of damage. Its "
                        "movement is based on its creature type (avian, swimmer, and so on). If your critter companion "
                        "dies, you can search an urban or wild environment for 1d6 days to find a new companion. "
                        "Enabler.",
                    "Face Morph":
                        "(2+ Intellect points) You alter your features and coloration for one hour, hiding your "
                        "identity or impersonating someone. This affects only your face, not the rest of your body. "
                        "You can’t perfectly duplicate someone else’s face, but you can be accurate enough to fool "
                        "someone who knows that person casually. You have an asset in all tasks involving disguise. "
                        "You must apply a level of Effort to be able to impersonate a different species. Action.",
                    "Fleet of Foot":
                        "(1+ Speed points) You can move a short distance as part of another action. You can move a "
                        "long distance as your entire action for a turn. If you apply a level of Effort to this "
                        "ability, you can move a long distance and make an attack as your entire action for a turn, "
                        "but the attack is hindered. Enabler.",
                    "Late Inspiration":
                        "(3 Intellect points) You retry a task you failed within the past one minute, using the same "
                        "difficulty and modifiers, except this time you have an asset on the task. If this retry "
                        "fails, you can’t use this ability to retry it again. Enabler.",
                    "Link Senses":
                        "(2 Intellect points) You touch a willing creature and link its senses to yours for one minute."
                        " At any time during that duration, you can concentrate to see, hear, and smell what that "
                        "creature is experiencing, instead of using your own senses. If you or the creature move out "
                        "of long range, the connection is broken. Action to initiate.",
                    "Phased Pocket":
                        "(2+ Intellect points) You connect yourself for one hour to a small space that is out of phase "
                        "and moves with you. You can access this space as if it were a convenient pocket or bag, but "
                        "nobody else can perceive or access the space unless they have the ability to interact with "
                        "transdimensional areas. The space can hold up to 1 cubic foot. The space is a part of you, "
                        "so you can’t use it to carry more cyphers than your limit, a detonation cypher activated "
                        "inside the space harms you, and so on. When the connection ends, anything in the space falls "
                        "out. For each 2 additional Intellect points you spend, the pocket lasts an additional hour. "
                        "Enabler.",
                    "Vanish":
                        "(2 Intellect points)You become invisible for a short amount of time. While invisible, you have"
                        " an asset on stealth and Speed defense tasks. The invisibility ends at the end of your next "
                        "turn, or if you do  something to reveal your presence or position—attacking, using an ability,"
                        " moving a large object, and so on. Action.",
                }
            },
            '2': {"Skills":
                    "You are trained in one task of your choosing (other than attacks or defense). If you choose a "
                    "task you’re already trained in, you become specialized in that task. You can’t choose a task "
                    "you’re already specialized in.",
                  "CHOOSE1": {
                     "Augment Cypher":
                         "(2+ Intellect points) When you activate a cypher, add +1 to its level. In addition to the "
                         "normal options for using Effort, you can choose to use Effort to increase the level of the "
                         "cypher by an additional +1 (per level of Effort applied). You can’t increase the cypher’s "
                         "level above 10. Enabler.",
                     "Create Debilitating Poison":
                         "(3+ Intellect points) You create one dose of a level 2 poison that hinders the poisoned "
                         "creature’s actions for ten minutes. You can apply this poison to a weapon, food, or drink as "
                         "part of the action of creating it. In addition to the normal options for using Effort, you "
                         "can choose to use Effort to increase the level of the poison; each level of Effort used in "
                         "this way increases the poison level by 1. If unused, the poison loses its potency after one "
                         "hour. Action.",
                     "Encouraging Presence":
                         "(2 Intellect points) For one minute, allies within short range gain an asset on defense "
                         "rolls. Action.",
                     "Illusory Duplicate":
                         "(2 Intellect points) You create a single image of yourself within immediate range. The image "
                         "looks like you as you are now (including how you are dressed). The image can move (for "
                         "example, you could make it walk or attack), but it can’t move more than an immediate "
                         "distance from where you created it. The illusion includes sound and smell. It lasts for ten "
                         "minutes and changes as you direct (no concentration is needed). If you move beyond short "
                         "range of the illusion, it vanishes. Action to create.",
                     "Intense Interaction":
                         "(3 Intellect points) You gain an asset on intimidating, persuading, and influencing people "
                         "for ten minutes. Action.",
                     "Restful Presence":
                         "Creatures who make a recovery roll within short range of you add +1 to their roll. Enabler.",
                     "Skill With Defense":
                         "Choose one type of defense task in which you are not already trained: Might, Speed, or "
                         "Intellect. You are trained in defense tasks of that type. Unlike most tricks of the trade, "
                         "you can select this trick up to three times. Each time you select it, you must choose a "
                         "different type of defense task. Enabler."
                 }},
            '3': {"Expert Cypher Use": "You can bear three cyphers at a time.",
                    "Skills":
                        "You are trained in one task of your choosing (other than attacks or defense). If you choose a "
                        "task you’re already trained in, you become specialized in that task. You can’t choose a task "
                        "you’re already specialized in.",
                    "CHOOSE1": {
                     "Far Hands":
                         "(2 Intellect points) You can use your tricks of the trade from one range category farther "
                         "away than normal: immediate becomes short, short becomes long, long becomes very long. Using "
                         "the trick at this increased distance hinders the task. Enabler.",
                     "Meticulous Planner":
                         "If you spend a long time planning an action, you gain an asset on performing it. The time to "
                         "study and plan for the action is ten times as long as it takes to perform the action. For "
                         "example, if you want to jump across a hole in the floor (one action), you can study the area "
                         "for ten rounds (about a minute), and when you attempt to jump over the hole, you have an "
                         "asset on the jump. This benefit applies to only one roll—if you want to perform the task "
                         "again with the benefit of an asset, you need to study and plan again. Enabler.",
                     "Obstacle Running":
                         "(3 Speed points): For the next minute, you can ignore obstacles that slow your movement, "
                         "allowing you to travel at normal speed through areas with rubble, fences, tables, and "
                         "similar objects that you would have to climb over or move around. This movement might "
                         "include sliding on a railing, briefly running along a wall, or even stepping on a creature "
                         "to boost yourself over something. If an obstacle would normally require a Might or Speed "
                         "task to overcome, such as swinging on a rope, balancing on a rope, or jumping over a hole, "
                         "you are trained at that task. Enabler.",
                     "Recharge Cypher (2+ Intellect points)":
                         "You recharge a cypher that was used in the past ten minutes, allowing it to be used again. "
                         "You must touch the cypher, spend 1 XP, and succeed at an understanding numenera roll "
                         "(difficulty equal to the level of the cypher) to recharge it. Otherwise, the cypher remains "
                         "spent and useless. Some cyphers (particularly pills and injections) cannot be recharged in "
                         "this way. In addition to the normal options for using Effort, you can choose to use Effort "
                         "to recharge a cypher that was used more than ten minutes ago; each level of Effort used in "
                         "this way extends the time period by ten minutes. Action.",
                     "Skill With Attacks":
                         "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                         "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or "
                         "heavy ranged. You are trained in attacks using that type of weapon. Enabler.",
                 }},
            '4': {"Skills":
                     "You are trained in one task of your choosing (other than attacks or defense). If you choose a "
                     "task you’re already trained in, you become specialized in that task. You can’t choose a task "
                     "you’re already specialized in.",
                 "CHOOSE1":{
                     "Bypass Barrier":
                         "(6+ Intellect points): You get past a door, force field, or other barrier up to 3 feet (1 m) "
                         "thick that is blocking your way. Depending on the barrier, this might involve finding a weak "
                         "spot you can push through, luckily pressing the right button, or even weirder explanations "
                         "like touching a thin place between dimensions or an unexpected interaction with numenera you "
                         "carry. The difficulty of the task is the level of the barrier. This trick allows you alone "
                         "to pass through, not anyone else, and the way through closes at the end of your turn (which "
                         "might mean you’re trapped on the far side). You have an asset in any attempts to get through "
                         "it again. In addition to the normal options for using Effort, you can choose to use Effort "
                         "to increase the maximum thickness of the barrier, each level adding 3 feet (1 m). Action.",
                     "Crowd Control":
                         "(6+ Intellect points) You control the actions of up to five creatures in short range. This "
                         "effect lasts for one minute. All targets must be level 2 or lower. Your control is limited "
                         "to simple verbal commands like 'stop,' 'run away,' 'follow that Glaive,' 'look over there,' "
                         "or 'get out of my way.' All affected creatures respond to the command unless you specifically"
                         " command them otherwise. In addition to the normal options for using Effort, you can choose "
                         "to use Effort to increase the maximum level of the targets or affect an additional five "
                         "people. Thus, to control a group that has a level 4 target (two levels above the normal "
                         "limit) or a group of fifteen people, you must apply two levels of Effort. When the Crowd "
                         "Control trick ends, the creatures remember your commands but don’t remember being controlled—"
                         " your commands seemed reasonable at the time. Action to initiate.",
                     "Illusory Evasion":
                         "(5 Intellect points) When you are hit by an attack, you teleport an immediate distance away, "
                         "leaving behind an illusory copy of yourself to be struck by that attack instead of you. This "
                         "destroys the illusion but leaves you unharmed by the attack. If the attack affects an area "
                         "and the teleportation can’t get you out of that area, the attack still affects you normally. "
                         "Enabler.",
                     "Memory Becomes Action":
                         "(4+ Intellect points) You can duplicate a one-action esotery, fighting move, or trick of the "
                         "trade, performing it as if it were natural for you. You must have seen the ability used "
                         "within the past week, it must be third tier or lower, and it must be an ability with a point "
                         "cost. In addition to the point cost of Memory Becomes Action, you must pay the Might, Speed, "
                         "or Intellect cost of the ability you are copying. In addition to the normal options for using"
                         " Effort, you can choose to use Effort to copy an ability you saw longer than one week ago; "
                         "each level of Effort used in this way extends the time period by one week. Enabler.",
                 }},
            '5': {"Adept Cypher Use": "You can bear four cyphers at a time.",
                 "Skills":
                     "You are trained in one task of your choosing (other than attacks or defense). If you choose a "
                     "task you’re already trained in, you become specialized in that task. You can’t choose a task "
                     "you’re already specialized in.",
                 "CHOOSE1": {
                     "Effective Skill":
                         "Choose one non-combat skill when you gain this ability. You get a minor effect with that "
                         "skill when you roll a natural 14 or higher (the d20 shows “14” or more). You get a major "
                         "effect with that skill when you roll a natural 19 or higher (the d20 shows “19” or higher). "
                         "Unlike most tricks of the trade, you can select this trick more than once. Each time you "
                         "select it, you must choose a different non-combat skill. Enabler.",
                     "Jaunt":
                         "(5+ Intellect points) You instantaneously teleport yourself to any location within a long "
                         "distance that you can  see. In addition to the normal options for using Effort, you can "
                         "choose to use Effort to increase the distance you can travel; each level of Effort used in "
                         "this way increases the range by another 100 feet (30 m). Action.",
                     "Mastery With Defense":
                         "Choose one type of defense task in which you are trained: Might, Speed, or Intellect. You "
                         "are specialized in defense tasks of that type. Unlike most tricks of the trade, you can "
                         "select this trick up to three times. Each time you select it, you must choose a different "
                         "type of defense task. Enabler.",
                     "Stun Attack":
                         "(6 Speed points) You attempt a difficulty 5 Speed action to stun a creature as part of your "
                         "melee or ranged attack. If you succeed, your attack inflicts its normal damage and stuns the "
                         "creature for one round, causing it to lose its next turn. If you fail, you still make your "
                         "normal attack roll, but you don’t stun the opponent if you hit. Action.",
                     "Subtle Tricks":
                         "You can use your skills and tricks of the trade in ways that don’t look like you’re doing "
                         "anything. If the skill or trick would normally require an obvious movement, phrase, or other "
                         "action by you, it instead seems to happen on its own. Instead of using your tools to pick a "
                         "lock, the lock clicks open as you stand near it. Instead of manipulating a numenera screen, "
                         "the information you want appears on the screen when you look at it. Instead of bluffing your "
                         "way past some guards, they step aside as you approach and let you through. This ability "
                         "usually only works up to an immediate distance. You still must spend points and make rolls "
                         "to use your skills and tricks with this ability. Performing a trick in a subtle way hinders "
                         "the task. This ability can’t be used to conceal your attack or defense rolls. Enabler.",
                     "Teach Trick":
                         "(5+ Intellect points) You spend an hour instructing someone on how to perform a trick of the "
                         "trade that you know. The trick must be no higher than fourth tier. For one hour after you "
                         "teach them, the student can perform that trick of the trade as if it were natural for them. "
                         "They must pay the Might, Speed, or Intellect cost (if any) to use that trick. The student "
                         "must be able to understand your instructions. In addition to the normal options for using "
                         "Effort, you can choose to use Effort to increase how long the student can use the trick or "
                         "to teach additional students at the same time; each level of Effort used in this way "
                         "increases the duration by one hour or the number of students by one. One hour to initiate.",
                 }},
            '6': {"Skills":
                     "You are trained in one task of your choosing (other than attacks or defense). If you choose a "
                     "task you’re already trained in, you become specialized in that task. You can’t choose a task "
                     "you’re already specialized in.",
                 "CHOOSE1":{
                     "Blurring Speed":
                         "(7 Speed points): You move so quickly that until your next turn, you look like a blur. While "
                         "you are blurred, if you apply Effort to a melee attack task or Speed defense task, you get a "
                         "free level of Effort on that task; you can move a short distance as part of another action "
                         "or a long distance as your entire action. Enabler.",
                     "Doppeljack":
                         "(7+ Might points) A perfect copy of you appears within an immediate distance. This "
                         "doppeljack might be a version of you from another timeline, a parallel dimension, or the "
                         "past; an instantly spawned clone; or something even stranger. The doppeljack is a level 6 "
                         "NPC with 18 health. It has your mind and memories, and you control it as if it were you in "
                         "another body. In effect, while this ability is active, you have two bodies. If the "
                         "doppeljack uses any of your abilities that cost points, those points come from your Pools "
                         "(including spending Effort). Controlling two bodies at once is difficult and distracting; "
                         "while this ability is active, all tasks performed by you or the doppeljack are hindered. The "
                         "doppeljack has no equipment other than simple clothing. It remains for up to one minute, but "
                         "disappears if killed or if you use an action to dismiss it. If the doppeljack is killed, you "
                         "take 6 points of damage that ignore Armor, and you lose your next action. If you are killed "
                         "while the doppeljack is present, you live on as the doppeljack (it becomes your character "
                         "instead of being an NPC that disappears). In addition to the normal options for using Effort,"
                         " you can choose to use Effort to increase the duration of this ability; each level of Effort "
                         "used in this way adds one minute to the doppeljack’s existence. Action.",
                     "Impossible Walk":
                         "(5+ Speed points): You can walk (or crawl or run) on steep inclines and horizontal surfaces "
                         "(such as walls and cliffs) for the next minute as if they were flat ground. When using this "
                         "ability, “down” for you is either the surface you are walking on or the normal orientation "
                         "of gravity (your choice). If you apply one level of Effort, you can also walk on the ceiling "
                         "or on a liquid or semi-liquid surface such as water, mud, quicksand, or even lava (although "
                         "touching a dangerous surface like lava still harms you). If you apply two levels of Effort, "
                         "you can also walk on air as if it were solid ground.",
                     "Mastery With Attacks":
                         "Choose one type of attack in which you are trained: light bashing, light bladed, light "
                         "ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or heavy "
                         "ranged. You are specialized in attacks using that type of weapon. Enabler. (In place of this "
                         "ability, you may instead select Skill With Attacks to become trained in one type of attack.)",
                     "Outside Reality":
                         "(6+ Intellect points): You exist outside of everything until the start of your next turn. To "
                         "you, a few seconds pass while you are alone in a cool void. To everyone else, you seem to "
                         "vanish for a few seconds and reappear in the same place. While in this unreal state, you can "
                         "use abilities or objects on yourself, but you can’t perceive, interact with, or affect the "
                         "rest of the world, and vice versa. Time-based effects already on you (like a poison that "
                         "inflicts damage every round) are paused while you exist outside reality, but when this "
                         "ability ends they resume as if no time had passed. In addition to the normal options for "
                         "using Effort, you can choose to use Effort to increase the duration; each level of Effort "
                         "used in this way adds one round to how long you spend outside reality. Enabler.",
                     "Rapid Recovery":
                         "You can make most recovery rolls faster than normal. You can make your one-action recovery "
                         "roll as part of another action or when it isn’t your turn, your ten-minute recovery roll "
                         "takes you only one action, and your one-hour recovery roll takes you only ten minutes (your "
                         "ten-hour rest is unchanged). If you make a recovery roll when it isn’t your turn, until the "
                         "end of your next turn all of your tasks are hindered. Enabler.",
                 }}
        }
    },
    "Arkus": {
        "Base Stats": [8, 9, 11],
        "Starting Edge": [0, 0, 1],
        "Weapon Proficiencies": ["Light"],
        "Class Skills": ["Persuasion", "CHOICE:Interaction Skill"],
        "Class Inabilities": ["Understanding Numenera", "Salvaging Numenera", "Crafting Numenera"],
        "Core Abilities": {"Demeanor of Command": ""},
        "Cypher Limit": 2,
        "Starting Equipment": [],
        "Default Cyphers": [],
        "Default Oddity": "",
        "Community Bonus": "",
        "Tiers": {
            '1': {},
            '2': {},
            '3': {},
            '4': {},
            '5': {},
            '6': {}
        }
    },
    "Wright": {
        "Base Stats": [9, 7, 12],
        "Starting Edge": [0, 0, 1],
        "Weapon Proficiencies": ["Light"],
        "Class Skills": ["Crafting Numenera", "CHOICE:Crafting Skill"],
        "Class Inabilities": ["Understanding Numenera", "Salvaging Numenera"],
        "Core Abilities": {},
        "Cypher Limit": 3,
        "Starting Equipment": [],
        "Default Cyphers": [],
        "Default Oddity": "",
        "Community Bonus": "",
        "Tiers": {
            '1': {},
            '2': {},
            '3': {},
            '4': {},
            '5': {},
            '6': {}
        }
    },
    "Delve": {
        "Base Stats": [9, 9, 10],
        "Starting Edge": [0, 1, 1],
        "Weapon Proficiencies": ["Light", "Medium"],
        "Class Skills": ["Salvaging Numenera", "CHOICE:Exploration Skill"],
        "Class Inabilities": ["Understanding Numenera", "Crafting Numenera"],
        "Core Abilities": {},
        "Cypher Limit": 2,
        "Starting Equipment": [],
        "Default Cyphers": ["Phasing Gloves", "Travel Bubble"],
        "Default Oddity": "Shirt that displays your muscles, bones, and internal organs when you wear it",
        "Community Bonus": "",
        "Tiers": {
            '1': {},
            '2': {},
            '3': {},
            '4': {},
            '5': {},
            '6': {}
        }
    }
}

assignable_stat_points = 6

descriptor_template = {
    "Stat Bonuses": [0, 0, 0],
    "Skills":[],
    "Inabilities":[],
    "Features": {},
    "Additional Equipment": [],
    "Link to Starting Adventure": []
}

descriptors = {
    "Charming": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Positive Interactions", "Abilities that Influence the Minds of Others"],
        "Inabilities": ["Tasks Involving Lore, Knowledge, or Understanding", "Resisting Mental Attacks"],
        "Features": {"Contact": "You have an important contact who is in an influential position, such as a minor"
                                " noble, the captain of the town guard, an Aeon Priest, or the head of a large gang of"
                                " thieves."},
        "Additional Equipment": ["10 extra Shins"],
        "Link to Starting Adventure": ["You convinced one of the other PCs to tell you what they were doing",
                                       "You instigated the whole thing and convinced the others to join you",
                                        "One of the others did you a favor, and now you're repaying it",
                                        "There's a reward involved, and you need the money"]
    },
    "Clever": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Lies and Trickery", "Mental Effect Defense", "Identifying, or assessing danger, lies, quality, "
                                                                 "importance, function, or power."],
        "Inabilities": ["Lore, Knowledge, or Understanding"],
        "Features": {},
        "Additional Equipment": ["10 extra shins"],
        "Link to Starting Adventure": ["You convinced one of the other PCs to tell you what they were doing",
                                       "From afar, you observed that something interesting was going on.",
                                       "You talked your way into the situation because you thought it might "
                                       "earn some money.",
                                       "You suspect that the other PCs won’t succeed without you."]
    },
    "Graceful": {
        "Stat Bonuses": [0, 2, 0],
        "Skills": ["Balance and Careful Movement", "Physical Performing Arts", "Speed Defence"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in "
                                       "your best interest.",
                                       "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Intelligent": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["CHOICE: Knowledge Skill", "Remembering Things You Experienced Directly"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": ["One of the other PCs asked your opinion of the mission, knowing that if you "
                                       "thought it was a good idea, it probably was.",
                                       "You saw value in what the other PCs were doing.",
                                       "You believed that the task might lead to interesting discoveries.",
                                       "A colleague requested that you take part in the mission as a favor."]
    },
    "Learned": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["CHOICE: Knowledge Skill 1", "CHOICE: Knowledge Skill 2", "CHOICE: Knowledge Skill 3"],
        "Inabilities": ["Charm, Persuasion, or Etiquette"],
        "Features": {},
        "Additional Equipment": ["Two books on topics of your choice"],
        "Link to Starting Adventure": ["One of the other PCs asked you to come along because of your knowledge.",
                                       "You need money to fund your studies.",
                                       "You believed that the task might lead to interesting discoveries.",
                                       "A colleague requested that you take part in the mission as a favor."]
    },
    "Mystical": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Understanding Numenera"],
        "Inabilities": ["Charm", "Persuasion", "Deception"],
        "Features": {'Sense "Magic"': "You can sense whether the numenera is active in situations where its presence is"
                                      "not obvious. You must study an object or location closely for a minute to get a"
                                      " feel for whether the touch of the ancients is at work.",
                     "Esotry: Hedge Magic": "You can perform small tricks: temporarily change the color or basic "
                                            "appearance of a small object, cause small objects to float through the "
                                            "air clean a small area, mend a broken object, prepare (but not create) "
                                            "food, and so on. You can’t use Hedge Magic to harm another creature or "
                                            "object. Action."},
        "Additional Equipment": ["An Oddity, as determined by the GM"],
        "Link to Starting Adventure": ["A dream guided you to this point.", "You need money to fund your studies.",
                                       "You believed the mission would be a great way to learn more about the numenera.",
                                       "Various signs and portents led you here."]
    },
    "Mechanical": {
        "Stat Bonuses": [0, 0, 2],
        "Skills":["Understanding Numenera"],
        "Inabilities":["Charm", "Persuasion", "Deception"],
        "Features": {"Sense 'Magic'": "You can sense whether the numenera is active in situations where its presence is"
                     "not obvious. You must study an object or location closely for a minute to get a feel for whether"
                                      " the touch of the ancients is at work.",
                     "Esotry: Hedge Magic": "You can perform small tricks: temporarily change the color or basic "
                                            "appearance of a small object, cause small objects to float through the "
                                            "air clean a small area, mend a broken object, prepare (but not create) "
                                            "food, and so on. You can’t use Hedge Magic to harm another creature or "
                                            "object. Action."},
        "Additional Equipment": ["An Oddity, as determined by the GM"],
        "Link to Starting Adventure": ["A dream guided you to this point", "You need money to fund your studies",
                                       "You believed the mission would be a great way to learn more about the numenera",
                                       "Various signs and portents led you here"]
    },
    "Rugged": {
        "Stat Bonuses": [0,0,0],
        "Skills": ["Climbing", "Jumping", "Running", "Swimming", "Training Natural Animals", "Riding Natural Animals",
                   "Placating Natural Animals", "Identifying and Using Natural Plants"],
        "Inabilities": ["Charm and Persuasion", "Etiquette", "Deception"],
        "Features": {},
        "Additional Equipment": ["An Explorer's Pack"],
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in your "
                                       "best interest.", "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Stealthy": {
        "Stat Bonuses": [0,2,0],
        "Skills": ["Stealthy Tasks", "Lies and Trickery", "Abilities involving Lies or Trickery"],
        "Inabilities": ["Movement-Related Tasks"],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": ["You attempted to steal from one of the other PCs. That character caught you and"
                                       " forced you to come along with them.",
                                       "You were tailing one of the other PCs for reasons of your own, which brought"
                                       " you into the action.", "An NPC employer secretly paid you to get involved.",
                                       "You overheard the other PCs talking about a topic that interested you, so you"
                                       " decided to approach the group."]
    },
    "Strong": {
        "Stat Bonuses": [4, 0, 0],
        "Skills": ["Breaking Inanimate Objects", "Jumping"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": ["Extra Medium or Heavy Weapon"],
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in your"
                                       " best interest.", "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Strong-willed": {
        "Stat Bonuses": [0, 0, 4],
        "Skills": ["Resisting Mental Effects", "Focus and Concentration"],
        "Inabilities": ["Puzzles and Problems", "Lore", "Memorization"],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in your"
                                       " best interest.", "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Swift": {
        "Stat Bonuses": [0, 4, 0],
        "Skills": ["Initiative", "Running"],
        "Inabilities": ["Balance"],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in your"
                                       " best interest.", "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Tough": {
        "Stat Bonuses": [0, 0, 0],
        "Skills":["Might Defense"],
        "Inabilities":[],
        "Features": {"Resilient": "Armor + 1", "Healthy": "Add 1 to your recovery rolls"},
        "Additional Equipment": ["Extra Light Weapon"],
        "Link to Starting Adventure": ["You’re acting as a bodyguard for one of the other PCs.",
                                       "One of the PCs is your sibling, and you came along to watch out for them.",
                                       "You need money because your family is in debt.",
                                       "You stepped in to defend one of the PCs when they were threatened. While "
                                       "talking to them afterward, you heard about the group’s task."]
    },
    "Adaptable": {

    },
    "Articulate": {},
    "Beneficent": {},
    "Cheerful": {},
    "Civic": {},
    "Committed": {},
    "Confident": {},
    "Cultured": {},
    "Curious": {},
    "Earnest": {},
    "Empirical": {},
    "Exacting": {},
    "Forward-Thinking": {},
    "Gregarious": {},
    "Heroic": {},
    "Imaginative": {},
    "Industrious": {},
    "Intimidating": {},
    "Intuitive": {},
    "Irrepressible": {},
    "Lawful": {},
    "Loyal": {},
    "Meddlesome": {},
    "Nurturing": {},
    "Obsessive": {},
    "Optimistic": {},
    "Organized": {},
    "Passionate": {},
    "Persevering": {},
    "Prepared": {},
    "Protective": {},
    "Relentless": {},
    "Risk-taking": {},
    "Serene": {},
    "Vicious": {}
}

focus_template = {
    "Description": "",
    "Connection": [],
    "Additional Equipment": [],
    "Core Features": {},
    "Major Effect Suggestions": "",
    "Minor Effect Suggestions": "",
    "Tier": {
        '1': {},
        '2': {},
        '3': {},
        '4': {},
        '5': {},
        '6': {}
    }
}

foci = {
    "Bears a Halo of Fire": {
        "Description": "You can create a sheath of flames around your body. You leave scorch marks wherever you go, "
                       "and you can’t handle combustible objects without first dousing your inherent flames. Your "
                       "special abilities (such as Nano esoteries) are tainted with flame. Fiery visuals accompany "
                       "your powers, and in some cases, your predilection for flame actually reshapes your abilities "
                       "to take on a fiery nature where none existed before.",
        "Connection": ["Pick one other PC. Through a quirk of fate, your fire cannot harm that character.",
                       "Pick one other PC. You burned this character by accident, and they still have a scar.",
                       "Pick one other PC. You’re always trying to impress them with your fire, but you’re not sure "
                       "why.",
                       "Pick one other PC.When you’re near this character, sometimes your flames burn with"
                       " weird patterns."],
        "Additional Equipment": ["An artifact: a device that sprays inanimate objects to make them fire-resistant. All "
                                 "your starting gear has already been treated unless you don’t want it to be."],
        "Core Features": {"Fire Powers": "Your special abilities that would normally use force or other energy (such as"
                                         " electricity) instead use fire. For example, force blasts from Onslaught are "
                                         "blasts of flame, and Flash is a burst of fire. These alterations change "
                                         "nothing except the type of damage and the fact that it might start fires."},
        "Major Effect Suggestions": "An important item on the target’s person is destroyed.",
        "Minor Effect Suggestions": "The target or something near the target catches fire.",
        "Tier": {
            '1': {"Shroud of Flame (1 Intellect point)":
                    "At your command, your entire body becomes shrouded in flames that last up to ten minutes. The "
                    "fire doesn’t burn you, but it automatically inflicts 2 points of damage to anyone who tries to "
                    "touch you or strike you with a melee attack. Flames from another source can still hurt you. "
                    "While the shroud is active, you gain +2 points of Armor that protect only against damage from "
                    "fire from another source. Enabler."},
            '2': {"Hurl Flame (2 Intellect points)":
                      "While your Shroud of Flame is active, you can reach into your halo and hurl a handful of fire "
                      "at a target. This is a ranged attack with short range that deals 4 points of fire damage."
                      " Action.",
                  "Fiery Power": "When you use the Onslaught force blast esotery or the Flash esotery, increase the "
                                 "damage by 1 point.If you don’t have either of those abilities, this ability has no "
                                 "effect.Fiery Power does not affect damage from the Onslaught mindslice. Enabler."},
            '3': {"CHOICE": {"Fiery Hand of Doom (3 Intellect points)":
                                 "While your Shroud of Flame is active, you can reach into your halo and produce a hand"
                                 " made of animate flame that is twice the size of a human’s hand. The hand acts as "
                                 "you direct, floating in the air. Without a command, the hand does nothing. It can "
                                 "move a long distance in a round, but it never moves farther away from you than long"
                                 " range. The hand can grab, move, and carry things, but anything it touches takes 1 "
                                 "point of damage per round from the heat. The hand can also attack. It’s a level 3 "
                                 "creature and deals 1 extra point of damage from fire when it attacks. Once created, "
                                 "the hand lasts for ten minutes. Action to create; action to direct.",
                             "Wings of Fire (4 Intellect points)":
                                 "While your Shroud of Flame is active, you can spread wings of fire and can levitate, "
                                 "moving at a rate of up to 20 feet(6 m) per round in any direction for one minute. You"
                                 " can also take one other non- movement action on your turn. Action."}
                  },
            '4': {"Flameblade (4 Intellect points)":
                      "When you wish it, you extend your halo of fire to cover a weapon  you wield in flame for one "
                      "hour. The flame ends if you stop holding or carrying the weapon. While the flame lasts, the "
                      "weapon inflicts 2 additional points of damage. Enabler."},
            '5': {"Fire Tendrils (5 Intellect points)":
                      "When you wish it, your halo sprouts three tendrils of flame that last for up to ten minutes. As "
                      "an action, you can use the tendrils to attack, making a separate attack roll for each. Each "
                      "tendril inflicts 4 points of damage. Otherwise, the attacks function as standard attacks. If "
                      "you don’t use the tendrils to attack, they remain but do nothing. Enabler."},
            '6': {"CHOICE": {"Fire Servant (6 Intellect points)":
                                 "You reach into your halo and produce an automaton of fire that is your general shape "
                                 "and size. It acts as you direct each round. Directing the servant is an action, and "
                                 "you can command it only when you are within long range of it. Without a command, the "
                                 "servant continues to follow your previous command. You can also give it a simple "
                                 'programmed action, such as "Wait here, and attack anyone who comes within short '
                                 'range until they’re dead." The servant lasts for ten minutes, is a level 5 creature, '
                                 "and deals 1 extra point of damage from fire when it attacks. Action to create; action"
                                 " to direct.",
                             "Inferno Trail (6 Intellect points)":
                                 "For the next minute, you leave a trail of flame in your wake. The trail matches your "
                                 "path and lasts for up to a minute, creating a wall of flame about 6 feet (2 m) high "
                                 "that inflicts 5 points of damage to any creature that passes through it, potentially "
                                 "catching them on fire for an additional 1 point of damage each round ( if they are "
                                 "flammable) until they spend a round putting out the fire.Action."}
                  }
        }
    },
    "Commands Mental Powers": {
        "Description": "You have always had special abilities that others didn’t seem to share. Through practice and "
                       "devotion, you have honed this unique talent so that you can harness the power of your mind to"
                       " perform deeds.",
        "Connection": ["Pick one other PC. You have found that this character is particularly tuned into your mental "
                       "powers. While you’re within short range of them, the two of you are always in telepathic "
                       "contact, and they are never harmed by your Psychic Bursts.",
                       "Pick one other PC. For some reason, you can’t telepathically interact with them.",
                       "Pick one other PC. That character and you always enjoy the effect of your Telepathic ability "
                       "even when you haven’t triggered it.",
                       "Pick one other PC.When they stand next to you and use their action to concentrate on helping "
                       "you, your Telepathic ability extends to a very long range."
                       ],
        "Additional Equipment": ["A crystal or jewel artifact that, when worn against your forehead or temple, adds 1 "
                                 "point to your Intellect Pool. If you’re ever without the artifact, subtract 5 points "
                                 "from your Intellect Pool; the points are restored if you regain the item."],
        "Core Features": {"Mental Esoteries": "When you apply Effort to the special abilities that control minds, like "
                                             "the Mind Control esotery, the Mind Reading esotery, or the Crowd Control "
                                             "trick of the trade, you get a free level of Effort on that task. "
                                              "Enabler."},
        "Major Effect Suggestions":"You can take another action on that same turn.",
        "Minor Effect Suggestions":"The range or duration of the mental power is doubled.",
        "Tier": {
            '1': {"Telepathic (1+ Intellect points)":
                      "You can speak telepathically with others who are within short range. Communication is two-way, "
                      "but the other party must be willing and able to communicate. You don’t have to see the target, "
                      "but you must know that it’s within range. You can have more than one active contact at once, "
                      "but you must establish contact with each target individually. Each contact lasts up to ten "
                      "minutes. If you apply a level of Effort to increase the duration rather than affect the "
                      "difficulty, the contact lasts for 28 hours. Action to establish contact."},
            '2': {"Mind Reading":
                      "(2 Intellect points)"
                      "You can read the surface thoughts of a creature within short range, even if the target doesn’t "
                      "want you to. You must be able to see your target. Once you have established contact, you can "
                      "read the target’s thoughts for up to one minute. If you also have the Mind Reading special "
                      "ability from your type, you can use this ability at long range, and you don’t need to be able "
                      "to see the target(but you do have to know that the target is within range). Action to "
                      "initiate."},
            '3': {"CHOICE": {"Psychic Burst":
                             "(3+ Intellect points)"
                             "You blast waves of mental force into the minds of up to three targets within short "
                             "range (make an Intellect roll against each target). This burst inflicts 3 points of "
                             "Intellect damage (and thus ignores Armor). For each 2 additional Intellect points you "
                             "spend, you can make an Intellect attack roll against an additional target. Action.",
                             "Psychic Suggestion":
                             "(4 Intellect points) "
                             "You attempt to make the target take the action you indicate on its next turn. If the "
                             "action you wish the target to take would cause direct harm to the target or its "
                             "allies, your mental attack is hindered. Action."}
                  },
            '4': {"Use Senses of Others":
                      "(4 Intellect points)"
                      "You can see, hear, smell, touch, and taste through the senses of anyone with whom you have "
                      "telepathic contact. You can attempt to use this ability on a willing or unwilling target within "
                      "long range; an unwilling target can try to resist. You don’t need to see the target, but you "
                      "must know that it’s within range. Your shared senses last ten minutes. Action to establish."},
            '5': {"Precognition":
                      "(6 Intellect points) "
                      "You dimly sense the future for the next ten minutes. This has the following effects until the "
                      "duration expires: Your defense tasks gain an asset; You can predict the actions of those around "
                      "you. You gain an asset to seeing through deceptions and attempts to betray you as well as "
                      "avoiding traps and ambushes; You know what people are probably thinking and what they will say "
                      "before they say it, which gives you an edge. You gain an asset to all interaction skills. "
                      "Enabler."},
            '6': {"CHOICE": {"Mind Control":
                                 "(6+ Intellect points)"
                                 "You control the actions of another creature you touch. This effect lasts for one "
                                 "minute. The target must be level 2 or lower. Once you have established control, you "
                                 "maintain mental contact with the target and sense what it senses. You can allow it "
                                 "to act freely or override its control on a case-by- case basis. In addition to the "
                                 "normal options for using Effort, you can choose to use Effort to increase the maximum"
                                 " level of the target or increase the duration by one minute. Thus, to control the "
                                 "mind of a level 5 target (three levels above the normal limit) or control a target "
                                 "for four minutes (three levels above the normal duration), you must apply three "
                                 "levels of Effort. If you also have the Mind Control special ability from your type, "
                                 "the normal level limit is 3 rather than 2. When the effect ends, the creature "
                                 "doesn’t remember being controlled or anything it did while under your command. "
                                 "Action to initiate.",
                             "Telepathic Network":
                                 "(0+ Intellect points) "
                                 "When you wish it, you can contact up to ten creatures known to you, no matter where "
                                 "they are. All targets must be willing and able to communicate. You automatically "
                                 "succeed at establishing a telepathic network; no roll is required. All creatures in "
                                 "the network are linked and can communicate telepathically with one another. They can "
                                 "also “overhear” anything said in the network, if they wish. Activating this ability "
                                 "doesn’t require an action and doesn’t cost Intellect points; to you, it’s as easy as "
                                 "speaking out loud. The network lasts until you choose to end it. If you spend 5 "
                                 "Intellect points, you can contact twenty creatures at once, and for every 1 Intellect"
                                 " point you spend above that, you can add ten more creatures to the network. These "
                                 "larger networks last for ten minutes. Creating a network of twenty or more creatures "
                                 "does require an action to establish contact. Enabler."
                             }
                  }
        },
    },
    "Controls Beasts": {
        "Description":
            "To say that you have a way with animals and nonhuman creatures doesn’t begin to cover it. Your mastery "
            "and communication with beasts is positively uncanny. They come to you fearlessly, and it’s not uncommon "
            "for birds to alight on your shoulder or for small animals to climb up your arms or legs.",
        "Connection":
            ["Pick one other PC. That character seems to disturb your creatures in a way that you can’t explain. You "
             "know that you must keep your animals away from them if possible, or you might lose control.",
             "Pick one other PC. The creature that you’re bonded with seems to have a special bond with this other "
             "person as well. You must decide whether it brings up feelings of jealousy or camaraderie within you and "
             "whether to thwart the connection or help it blossom.",
             "Pick one other PC. Recently, they accidentally (or perhaps intentionally) put your beast companion in a "
             "position of danger. Your companion is now nervous around them, and you are struggling with your own "
             "emotional response to the incident.",
             "Pick one other PC. They dislike beasts of all kinds, seeing them as little more than food or prey. You "
             "hope that exposing them to your beast companion will change their mind. It’s up to that player how their "
             "character responds to the experience."],
        "Additional Equipment": ["3 days of food for your Animal Companion", "Leash, Collar, or equivalent"],
        "Core Features": {},
        "Major Effect Suggestions": "The duration of calmness or control extends to 28 hours.",
        "Minor Effect Suggestions": "The duration of calmness or control is doubled.",
        "Tier": {
            '1': {"Beast Companion":
                      "A level 2 creature of your size or smaller accompanies you and follows your instructions. You "
                      "and the GM must work out the details of your creature, and you’ll probably make rolls for it in "
                      "combat or when it takes actions. The beast companion acts on your turn. As a level 2 creature, "
                      "it has a target number of 6 and 6 health and it inflicts 2 points of damage. Its movement is "
                      "based on its creature type (avian, swimmer, and so on). If your beast companion dies, you can "
                      "hunt in the wild for 1d6 days to find a new companion. Enabler."},
            '2': {"Soothe the Savage":
                      "(2 Intellect points) You calm a nonhuman beast within 30 feet (9m). You must speak to it "
                      "(although it doesn’t need to understand your words), and it must see you. It remains calm for "
                      "one minute or for as long as you focus all your attention on it. The GM has final say over what "
                      "counts as a nonhuman beast, but unless some kind of deception is at work, you should know "
                      "whether you can affect a creature before you attempt to use this ability on it. Aliens, "
                      "extradimensional entities, very intelligent creatures, and automatons never count. Action.",
                  "Communication":
                      "(2 Intellect points) You can convey a basic concept to a creature that normally can’t speak or "
                      "understand speech. The creature can also give you a very basic answer to a simple question. "
                      "Action."},
            '3': {"CHOICE": {
                "Mount":
                    "A level 3 creature serves you as a mount and follows your instructions. While you’re mounted on "
                    "it, the creature can move and you can attack on your turn, which provides an asset to your attack."
                    " You and the GM must work out the details of the creature, and you’ll probably make rolls for it "
                    "when it takes non- combat actions. The mount acts on your turn. If your mount dies, you can hunt "
                    "in the wild for 3d6 days to find a new one. Enabler.",
                "Stronger Together":
                    "When you and your beast are within immediate distance of each other, you inflict 2 additional "
                    "points of damage when you attack and both of you gain an asset to defense actions. Enabler."
            }},
            '4': {"Beast Eyes":
                      "(3 Intellect points). You can sense through your beast companion’s senses if it is within 1 "
                      "mile (1.5 km) of you. This effect lasts up to ten minutes. Action to establish.",
                  "Improved Companion":
                      "Your beast companion increases to level 4. As a level 4 creature, it has a target number of 12 "
                      "and 12 health, and it inflicts 4 points of damage (though in most cases, instead of attacking, "
                      "it provides an asset to your attacks). Enabler.",},
            '5': {"Beast Call":
                      "(5 Intellect points) You summon a horde of small animals or a single level 4 beast to help you "
                      "temporarily. These creatures do your bidding for as long as you focus your attention, but you "
                      "must use your action each turn to direct them. Creatures are native to the area and arrive "
                      "under their own power, so if you’re in an unreachable place, this ability won’t work. Action."},
            '6': {"Improved Companion":
                      "Your beast companion increases to level 5. As a level 5 creature, it has a target number of 15 "
                      "and 15 health, and it inflicts 5 points of damage. Enabler.",
                  "CHOICE": {
                      "As If One Creature":
                          "When you and your beast are within immediate distance of each other, you can share damage "
                          "inflicted on either of you. For instance, if one of you is struck by a weapon for 4 points "
                          "of damage, divide the damage between the two of you as you see fit. Only the Armor and "
                          "resistances of the target initially damaged come into play. So if you have 2 Armor and are "
                          "struck by a force blast for 4 points of damage, your beast can take the 2 points of damage "
                          "you would suffer, but their Armor does not come into play, nor does their immunity to force "
                          "blasts, if any. Enabler.",
                      "Control the Savage":
                          "(6 Intellect points). You can control a calm nonhuman beast within 30 feet (9 m). You "
                          "control it for as long as you focus all your attention on it, using your turn each round. "
                          "The GM has final say over what counts as a nonhuman beast, but unless some kind of "
                          "deception is at work, you should know whether you can affect a creature before you attempt "
                          "to use this ability on it. Aliens, extradimensional entities, very intelligent creatures, "
                          "and automatons never count. Action."
                  }}
        }
    },
    "Controls Gravity":{
        "Description":
            "Gravity must have been quite a concern for the people of prior epochs because thereare many paths within "
            "the numenera to control it. Through a quirk of fate, some unique device(s), or supreme devotion (or a "
            "combination of all three), you have learned to tap into the power of gravity. With one foot planted in "
            "the distant past, you are a mysterious individual. Most likely, you are also older, having spent much of "
            "your life honing your odd, ancient talents.",
        "Connection":
            ["Pick one other PC. In the recent past, while using your gravitational powers, you accidentally sent that "
             "character hurtling into the air or plummeting toward the ground. Either way, they barely survived. It is "
             "up to the player of that character to decide whether they resent, fear, or forgive you.",
             "Pick one other PC whose focus intertwines with yours. This odd connection affects them in some way. For "
             "example, if the character uses a bow, your ability to manipulate gravity sometimes extends the range of "
             "their arrows.If they are good at jumping, they seem less bound by the laws of gravity, and jump farther.",
             "Pick one other PC. They are deathly afraid of heights. Through your ability to control gravity, you "
             "would like to teach them how to be more comfortable with their feet off the ground. They must decide "
             "whether or not to take you up on your offer.",
             "Pick one other PC. They are skeptical of your ability to control gravity and think it’s just one big "
             "illusion. They might even attempt to discredit you or discover the “secret” behind your so-called "
             "skills."],
        "Additional Equipment": ["a pen-sized oddity that tells the weight of whatever you point it at (within short "
                                 "range). The weight is displayed on a small glass plate in runes that only you can "
                                 "decipher."],
        "Core Features": {"Gravity Ability":
                             "You can choose to learn Weighty instead of one of the abilities granted by your type: "
                             "Weighty (1 Intellect point): You briefly increase the weight of a target within short "
                             "range enough to stop them in their tracks, preventing the target from moving and "
                             "hindering any attempted tasks on their next turn. Action."},
        "Major Effect Suggestions": "The duration of the effect is doubled.",
        "Minor Effect Suggestions": "An important item on the target’s person is destroyed.",
        "Tier": {
            '1': {"Hover":
                      "(1 Intellect point) You float slowly into the air. As your action, you can concentrate to remain"
                      " motionless in the air, or float up to a short distance, but no more; otherwise, you drift with "
                      "the wind or with any momentum you have gained. This effect lasts for up to ten minutes. If you "
                      "also have the Hover ability granted by your type, you can hover for twenty minutes and move "
                      "your normal speed. Action to initiate."},
            '2': {"Lessening Gravity’s Pull": "By manipulating gravity’s pull on yourself, you gain +1 to your Speed "
                                              "Edge. Enabler."},
            '3': {"CHOICE": {
                "Define Down":
                    "(4 Intellect points). The natural gravity within an area a short distance across that you are "
                    "within immediate range of changes directions so that it flows in the direction you determine (up, "
                    "up and to the south, west, and so on) for a few seconds, then snaps back. Affected targets could "
                    "be tossed up to 20 feet (6 m) and take a few points of damage. Action.",
                "Gravity Cleave":
                    "(3 Intellect points). You can harm a target within short range by rapidly increasing gravity’s "
                    "pull on one portion of the target and decreasing it on another, inflicting 6 points of damage. "
                    "Action."
            }},
            '4': {"Field of Gravity":
                      "(4 Intellect points). When you wish it, a field of manipulated gravity around you pulls incoming"
                      " ranged projectile attacks to the ground. You are immune to such attacks until your turn in the "
                      "next round. You must be aware of an attack to foil it. This ability does not work on energy "
                      "attacks. Enabler."},
            '5': {"Flight":
                      "(4+ Intellect points). You can float and fly through the air for one hour. For each level of "
                      "Effort applied, you can affect one additional creature of your size or smaller. You must touch "
                      "the creature to bestow the power of flight. You direct the other creature’s movement, and while "
                      "flying, it must remain within sight of you or fall. In terms of overland movement, a flying "
                      "creature moves about 20 miles (32 km) per hour and is not affected by terrain. Action to "
                      "initiate."},
            '6': {"CHOICE": {
                "Improved Gravity Cleave":
                    "(9 Intellect points) You can harm a group of targets within long range by rapidly increasing "
                    "gravity’s pull on one portion of each target and decreasing it on another, inflicting 6 points of "
                    "damage. The targets must be within immediate range of each other. Action.",
                "Weight of the World":
                    "(6+ Intellect points) You can increase a target’s weight dramatically. The target is pulled to the"
                    " ground and can’t move physically under its own power for one minute. The target must be within "
                    "short range. For each level of Effort applied, you can affect one additional creature. Action."
            }}
        }
    },
    "Crafts Illusions":{
        "Description": "You use the numenera to create holographic images that appear real. You are, in effect, an "
                       "artist—a crafter of light and sound. Holographic images can never inflict direct harm or exert "
                       "real force, but they can fool creatures, changing opinions and even behaviors if you craft "
                       "them cleverly.",
        "Connection": ["Pick one other PC. This character is never fooled by your illusions and is never affected by "
                       "the trickery of your special abilities. You can choose whether or not you know this fact.",
                       "Pick one other PC. They have a special angle on your illusions and can sometimes point out "
                       "potential places of weakness.",
                       "Pick two other PCs who are willing to be trained as your assistants. When you use your Minor "
                       "Illusion ability, if both of these characters are in immediate range, they can assist you, "
                       "working together to ease your action.",
                       "Pick one other PC. That character’s face is so intriguing to you in a way you don’t understand "
                       "that your minor illusions sometimes look like them, even when you don’t intend them to."],
        "Additional Equipment": ["An oddity that appears to be a piece of clear glass in a synth frame. By manipulating"
                                " hidden switches on the frame, you can make random moving images appear on the glass. "
                                "The images are usually strange and sometimes incomprehensible."],
        "Core Features": {"Psychedelic Abilities":
                             "Your special abilities take on flamboyant visual and auditory qualities of your choosing."
                             " This alteration changes nothing other than the appearance of the effects. For example, "
                             "your attack esoteries might look like monsters made of energy that assail your foes. Your"
                             " Stasis esotery might look like a tentacled beast that holds the victim in place. Your "
                             "Teleportation esotery might seem like a hole in space opens up and swallows you. Your "
                             "Skill With Defense fighting move might look like ghostly echoes mimicking your actions or"
                             " ephemeral arms blocking attacks against you."},
        "Major Effect Suggestions": "The illusion lasts for one hour, or if it already lasts that long, it lasts for "
                                    "28 hours.",
        "Minor Effect Suggestions": "Your illusion has a special quality to it—perhaps an observer sees an image of "
                                    "something from their past.",
        "Tier": {
            '1': {"Minor Illusion":
                      "(1 Intellect point). You create a single image of a creature or object within immediate range. "
                      "The image must fit within a 10-foot (3 m) cube. The image can move (for example, you could make "
                      "the illusion of a person walk or attack), but it can’t leave the area defined by the cube. The "
                      "illusion includes sound but not smell. It lasts for ten minutes, but if you want to change the "
                      "original illusion significantly—such as making a creature appear to be wounded—you must "
                      "concentrate on it again (though doing so doesn’t cost additional Intellect points). If you move"
                      "beyond immediate range of the cube, the illusion vanishes. Action to create; action to modify."},
            '2': {"Disguise":
                      "(2+ Intellect points). You appear to be someone or something else, roughly of your size and "
                      "shape, for up to one hour. Once created, the disguise requires no concentration. For each "
                      "additional Intellect point you spend, you can disguise one other creature. All disguised "
                      "creatures must stay within sight of you or lose their disguise. Action to create."},
            '3': {"CHOICE": {
                "Cast Illusion":
                    "You can increase the range at which you create and maintain your immediate-range illusions to "
                    "anywhere within short range that you can perceive. Enabler.",
                "Major Illusion":
                    "(3 Intellect points). You create a complex scene of images within immediate range. The entire "
                    "scene must fit within a 100- foot (30 m) cube. The images can move, but they can’t leave the area "
                    "defined by the cube. The illusion includes sound and smell. It lasts for ten minutes and changes "
                    "as you direct (no concentration is needed). If you move beyond immediate range of the cube, the "
                    "illusion vanishes. Action to create."
            }},
            '4': {"Illusory Selves":
                      "(4 Intellect points). You create four holographic duplicates of yourself within short range. "
                      "The duplicates last for one minute. You mentally direct their actions, and the duplicates aren’t"
                      " mirror images—each one can do different things. If struck violently, they either disappear "
                      "permanently or freeze motionless (your choice). Action to create."},
            '5': {"Terrifying Image":
                      "(6 Intellect points) You use a bit of subtle telepathy to learn which images would appear "
                      "terrifying to creatures that you choose within long range. Those images appear within that area "
                      "and menace the appropriate creatures. Make an Intellect attack roll against each creature you "
                      "want to affect. Success means the creature flees in terror for one minute, pursued by its "
                      "nightmares. Failure means the creature ignores the images, which do not hamper it in any way. "
                      "Action."},
            '6': {"CHOICE":{
                "Grandiose Illusion":
                    "(8 Intellect points). You create a fantastically complex scene of images that fit within a 1-mile "
                    "(1.5 km) cube that you are also within. You must be able to see the images when you create them. "
                    "The images can move in the cube and act in accordance with your desires. They can also act "
                    "logically (such as reacting appropriately to fire or attacks) when you aren’t directly observing "
                    "them. The illusion includes sound and smell. For example, armies can clash in battle, with air "
                    "support from machines or flying creatures, on and above terrain of your creation. The illusion "
                    "lasts for one hour (or longer, if you concentrate on it after that time). Action.",
                "Permanent Illusion":
                    "(9 Intellect points). An illusion (or portion of an illusion) that you create that fits within a "
                    "10-foot (3 m) cube becomes permanent. You can permanently end the illusion as an action, but "
                    "others must expend exceptional ingenuity to prevent the illusion from regenerating even if it has "
                    "apparently been dispersed. Enabler."
            }}
        }
    },
    "Employs Magnetism": {},
    "Entertains": {},
    "Exists Partially Out of Phase": {},
    "Explores Dark Places": {},
    "Fights with Panache": {},
    "Fuses Flesh and Steel": {},
    "Howls at the Moon": {},
    "Hunts": {},
    "Lives in the Wilderness": {},
    "Masters Defense": {},
    "Masters Weaponry": {},
    "Murders": {},
    "Rages": {},
    "Rides the Lightning": {},
    "Speaks With a Silver Tongue": {},
    "Talks to Machines": {},
    "Wears a Sheen of Ice": {},
    "Weilds Power with Precision": {},
    "Wields Two Weapons at Once": {},
    "Works the Back Alleys": {},
    "Works Miracles": {},
    "Absorbs Energy": {},
    "Acts Without Consequence": {},
    "Adjures the Leviathan": {},
    "Augments Flesh with Grafts": {},
    "Battles Automatons": {},
    "Brandishes an Exotic Shield": {},
    "Breaks Down Walls": {},
    "Builds Tomorrow": {},
    "Dances with Dark Matter": {},
    "Defends the Gate": {},
    "Defends the Weak": {},
    "Descends From Nobility": {},
    "Emerged From The Obelisk": {},
    "Explores Yesterday": {},
    "Fights with a Hoarde": {},
    "Fuses Mind and Machine": {},
    "Hunts Abhumans": {},
    "Imparts Wisdom": {},
    "Leads": {},
    "Learns From Adversity": {},
    "Metes Out Justice": {},
    "Moves Like A Cat": {},
    "Needs No Weapons": {},
    "Never Says Die": {},
    "Possesses a Shard of the Sun": {},
    "Radiates Vitality": {},
    "Sees Beyond": {},
    "Shepards the Community": {},
    "Shreds the Walls of the World": {},
    "Thunders": {},
    "Touches the Sky": {},
    "Wields Words Like Weapons": {}
}

weapon_damages = {"Light": 2, "Medium": 3, "Heavy": 4}