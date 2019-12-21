
# Change Abilities so that pool costs are in the description rather than the Key?

type_template = {
    "Base Stats": [7, 7, 7],
    "Starting Edge": [0, 0, 0],
    "Weapon Proficiencies": [],
    "Class Skills": [],
    "Class Intrusions": {},
    "Cypher Limit": 2,
    "Starting Equipment": [],
    "Default Cyphers": [],
    "Default Oddity": [],
    "Community Bonus": [],
    "Connections": [],
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
        "Connections": [
            "You were in the military and have friends who still serve. Your former commander remembers you well.",
            "You were the personal guard of a wealthy merchant who accused you of theft. You left her service in "
            "disgrace.",
            "You were the bouncer in a local bar for a while, and the patrons there remember you.",
            "You trained with a highly respected mentor. He regards you well, but he has many enemies.",
            "You trained in an isolated monastery far away. The monks think of you as a brother, but you’re a "
            "stranger to all others.",
            "You have no formal training. Your abilities come to you naturally (or unnaturally).",
            "You spent time on the streets and even were in prison for a while.",
            "You were conscripted into military service, but you deserted before long.",
            "You served as a bodyguard to a powerful criminal who now owes you his life.",
            "You worked as a constable. Everyone knows you, but their opinions of you vary.",
            "Your older sibling is an infamous glaive who has been disgraced.",
            "You served as a caravan guard. You know a smattering of people in many cities and towns.",
            "Your best friend is a sage and a scholar. She is a great source of knowledge.",
            "You and a friend both smoke the same kind of rare, expensive tobacco. The two of you get together "
            "weekly to chat and smoke.",
            "Your uncle runs a theater in town. You know all the actors and watch all the shows for free.",
            "Your blacksmith friend sometimes calls on you for help at the forge. However, he pays you well.",
            "Your mentor wrote a book on the martial arts. Sometimes other warriors seek you out to ask about its "
            "stranger passages.",
            "A man you fought alongside in the military is now the mayor of a nearby town.",
            "You saved the lives of a family when their house burned down. They’re indebted to you, and "
            "their neighbors regard you as a hero.",
            "Your old trainer still expects you to come back and sharpen her blades and clean up after her "
            "classes, but when you do, she occasionally shares interesting rumors."],
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
                    "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
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
        "Class Intrusions": {"Advantageous Malfunction":
                                 "A numenera device that is being used against you malfunctions. It might harm the "
                                 "user or one of their allies for a round, or activate a dramatic and distracting side "
                                 "effect for a few rounds.",
                             "Convenient Glimmer":
                                 "A glimmer provides you with a clear answer or suggests a course of action with "
                                 "regard to an urgent question, problem, or obstacle you’re facing.",
                             "Inexplicably Unbroken":
                                 "An inactive, ruined, or presumed-destroyed device temporarily activates and performs "
                                 "a useful function relevant to the situation. This is enough to buy you some time for "
                                 "a better solution, alleviate a complication that was interfering with your "
                                 "abilities, or just get you one more use out of a depleted cypher or artifact."},
        "Starting Equipment": ["Clothing", "Weapon", "Book About The Numenera", "3 Cyphers", "1 Oddity"],
        "Default Cyphers": ["Gravity Nullifying Spray", "Telepathy Implant", "Teleporter"],
        "Default Oddity": "Infinity Thermos",
        "Community Bonus": "",
        "Connections": [
            "You served as an apprentice for a nano-sorcerer respected and feared by many people. Now you bear his "
            "mark.",
            "You studied in a school infamous for its dark, brooding instructors and graduates.",
            "You learned nano-sorcery (or gained your modifications) in the temple of an obscure god. Its priests and "
            "worshippers, although small in number, respect and admire your talents and potential.",
            "While traveling alone, you saved the life of a powerful abhuman brute. Although unwilling to accompany "
            "you on your journey, he remains indebted to you.",
            "Your mother was a powerful nano while she lived, helpful to many locals. They look upon you kindly, but "
            "they also expect much from you.",
            "You owe money to a number of people around town and don’t have the funds to pay your debts.",
            "You failed disgracefully at your initial studies with your teacher and now proceed on your own.",
            "You learned your skills faster than your teachers had ever seen before. The powers that be took notice "
            "and are paying close attention.",
            "You killed a well-known criminal in self-defense, earning the respect of many and the enmity of a "
            "dangerous few.",
            "You trained as a glaive, but your skills with the numenera and other types of lore eventually led you "
            "down a different path. Your former comrades don’t understand you, but they respect you.",
            "While studying to be a nano, you worked as an assistant for a seamstress, making friends with the owner "
            "and the clientele.",
            "Your family owns a large vineyard nearby known to all for its fine wine and fair business dealings.",
            "You trained for a time with a group of Aeon Priests, and they still look upon you with fondness.",
            "You worked the gardens in the palace of an influential noble. She wouldn’t remember you, but you made "
            "friends with her young daughter.",
            "An experiment you conducted in the past went horribly awry. The locals remember you as a dangerous and "
            "foolhardy individual.",
            "You hail from a distant land where you were well known and regarded, but people here treat you with "
            "suspicion.",
            "People you meet seem put off by the strange birthmark on your face.",
            "Your best friend is also a nano. You and she share discoveries and secrets readily.",
            "You know a local merchant very well. Since you give him so much business, he offers you discounts and "
            "special treatment.",
            "You belong to a secretive social club that gathers monthly to drink and talk.",
        ],
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
        "Starting Edge": "CHOICE",         # Choice: Add one edge to chosen pool
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
        "Connections": [
            "You come from a large family and had to fend for yourself from an early age.",
            "Your older sister is a skilled nano. You weren’t able to follow her path, but the numenera is not "
            "unknown to you.",
            "You’re a member of a guild of explorers who specialize in uncovering ancient mysteries.",
            "You worked alongside your father, who was skilled in many things, until he disappeared one day with no "
            "explanation.",
            "You grew up on the streets and studied at the school of hard knocks.",
            "You remember little of your past, which has always seemed strange to you.",
            "You came of age in the wild and are used to living rough.",
            "Your family is wealthy but earns little respect from the locals.",
            "You’re friends with many people in the community and are generally well regarded.",
            "You have an annoying rival who always seems to get in your way or foil your plans.",
            "You’re in love with a local shopkeeper, but that person shows little interest in you.",
            "Several expeditions preparing to explore old ruins and odd mysteries would like you to join them because "
            "you seem like a promising addition to the team.",
            "Your best friend from childhood is now an Aeon Priest.",
            "You come from a nearby community, but the locals consider the folk of your hometown to be untrustworthy "
            "rivals.",
            "You’re close friends with a local married couple, both of whom are experienced nanos.",
            "You’re drinking buddies with a number of the local guards and glaives.",
            "You once saved the child of a local noble from a fire, and she is very grateful.",
            "You used to work with a troupe of traveling minstrels and performers, and they remember you fondly "
            "(as do people in the places you visited).",
            "You’re wanted for a crime you didn’t commit.",
            "You have a friend with an extensive library, plenty of food and drink, and a comfortable home—and the "
            "door is always open to you.",
        ],
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
    },  # End Discovery Types, Begin Destiny Types
    "Arkus": {
        "Base Stats": [8, 9, 11],
        "Starting Edge": [0, 0, 1],
        "Weapon Proficiencies": ["Light"],
        "Class Skills": ["Persuasion", "CHOICE:Interaction Skill"],
        "Class Inabilities": ["Understanding Numenera", "Salvaging Numenera", "Crafting Numenera"],
        "Core Abilities": {"Demeanor of Command": ""},
        "Cypher Limit": 2,
        "Class Intrusions": {},
        "Starting Equipment": [],
        "Default Cyphers": [],
        "Default Oddity": "",
        "Community Bonus": "",
        "Connections": [],
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
        "Cypher Limit": 3,
        "Class Intrusions": {},
        "Starting Equipment": [],
        "Default Cyphers": [],
        "Default Oddity": "",
        "Community Bonus": "",
        "Connections": [],
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
        "Class Intrusions": {},
        "Starting Equipment": [],
        "Default Cyphers": ["Phasing Gloves", "Travel Bubble"],
        "Default Oddity": "Shirt that displays your muscles, bones, and internal organs when you wear it",
        "Community Bonus": "",
        "Connections": [],
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
        "Skills": ["Might Defense"],
        "Inabilities":[],
        "Features": {"Resilient": "Armor + 1", "Healthy": "Add 1 to your recovery rolls"},
        "Additional Equipment": ["Extra Light Weapon"],
        "Link to Starting Adventure": ["You’re acting as a bodyguard for one of the other PCs.",
                                       "One of the PCs is your sibling, and you came along to watch out for them.",
                                       "You need money because your family is in debt.",
                                       "You stepped in to defend one of the PCs when they were threatened. While "
                                       "talking to them afterward, you heard about the group’s task."]
    },  # End Discovery Descriptors, Begin Destiny Descriptors
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
    "Tiers": {
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
        "Tiers": {
            '1': {"Shroud of Flame":
                    "(1 Intellect point) "
                    "At your command, your entire body becomes shrouded in flames that last up to ten minutes. The "
                    "fire doesn’t burn you, but it automatically inflicts 2 points of damage to anyone who tries to "
                    "touch you or strike you with a melee attack. Flames from another source can still hurt you. "
                    "While the shroud is active, you gain +2 points of Armor that protect only against damage from "
                    "fire from another source. Enabler."},
            '2': {"Hurl Flame":
                      "(2 Intellect points) "
                      "While your Shroud of Flame is active, you can reach into your halo and hurl a handful of fire "
                      "at a target. This is a ranged attack with short range that deals 4 points of fire damage."
                      " Action.",
                  "Fiery Power": "When you use the Onslaught force blast esotery or the Flash esotery, increase the "
                                 "damage by 1 point.If you don’t have either of those abilities, this ability has no "
                                 "effect.Fiery Power does not affect damage from the Onslaught mindslice. Enabler."},
            '3': {"CHOICE": {"Fiery Hand of Doom":
                                 "(3 Intellect points) "
                                 "While your Shroud of Flame is active, you can reach into your halo and produce a hand"
                                 " made of animate flame that is twice the size of a human’s hand. The hand acts as "
                                 "you direct, floating in the air. Without a command, the hand does nothing. It can "
                                 "move a long distance in a round, but it never moves farther away from you than long"
                                 " range. The hand can grab, move, and carry things, but anything it touches takes 1 "
                                 "point of damage per round from the heat. The hand can also attack. It’s a level 3 "
                                 "creature and deals 1 extra point of damage from fire when it attacks. Once created, "
                                 "the hand lasts for ten minutes. Action to create; action to direct.",
                             "Wings of Fire":
                                 " (4 Intellect points)"
                                 "While your Shroud of Flame is active, you can spread wings of fire and can levitate, "
                                 "moving at a rate of up to 20 feet(6 m) per round in any direction for one minute. You"
                                 " can also take one other non- movement action on your turn. Action."}
                  },
            '4': {"Flameblade":
                      "(4 Intellect points)"
                      "When you wish it, you extend your halo of fire to cover a weapon  you wield in flame for one "
                      "hour. The flame ends if you stop holding or carrying the weapon. While the flame lasts, the "
                      "weapon inflicts 2 additional points of damage. Enabler."},
            '5': {"Fire Tendrils":
                      "(5 Intellect points)"
                      "When you wish it, your halo sprouts three tendrils of flame that last for up to ten minutes. As "
                      "an action, you can use the tendrils to attack, making a separate attack roll for each. Each "
                      "tendril inflicts 4 points of damage. Otherwise, the attacks function as standard attacks. If "
                      "you don’t use the tendrils to attack, they remain but do nothing. Enabler."},
            '6': {"CHOICE": {"Fire Servant":
                                 "(6 Intellect points)"
                                 "You reach into your halo and produce an automaton of fire that is your general shape "
                                 "and size. It acts as you direct each round. Directing the servant is an action, and "
                                 "you can command it only when you are within long range of it. Without a command, the "
                                 "servant continues to follow your previous command. You can also give it a simple "
                                 'programmed action, such as "Wait here, and attack anyone who comes within short '
                                 'range until they’re dead." The servant lasts for ten minutes, is a level 5 creature, '
                                 "and deals 1 extra point of damage from fire when it attacks. Action to create; action"
                                 " to direct.",
                             "Inferno Trail":
                                 "(6 Intellect points)"
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
        "Tiers": {
            '1': {"Telepathic":
                      "(1+ Intellect points)"
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
        "Tiers": {
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
    "Controls Gravity": {
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
        "Tiers": {
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
        },
    },
    "Crafts Illusions": {
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
        "Tiers": {
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
    "Employs Magnetism": {
        "Description": "Electromagnetism is a fundamental force in the universe, and it is yours to command. You are "
                       "a master of metal.",
        "Connection": [
            "Pick one other PC. Whenever you use your powers, the metallic items on that character’s body shudder, "
            "rattle, clink, and shake if they are within short range.",
            "Pick one other PC. You worked together in the past, and the job ended badly.",
            "Pick two other PCs. While practicing your Diamagnetism ability, you once accidentally sent them "
            "careening into each other. You’ve never been able to repeat it. Whether you tell them that you’ve been "
            "trying to replicate the strange effect is up to you.",
            "Pick one other PC who has metallic elements in their body. You’re afraid to use your magnetism abilities "
            "near them because you once had a bad experience involving Move Metal and a (probably former) friend’s "
            "mechanical eyes.",
        ],
        "Additional Equipment": [],
        "Core Features": {},
        "Major Effect Suggestions": "An important item on the target’s person is destroyed.",
        "Minor Effect Suggestions": "The duration of the effect is doubled.",
        "Tiers": {
            '1': {
                "Move Metal":
                      "(1 Intellect point) You can exert force on metal objects within short range for one round. "
                      "Once activated, your power has an effective Might Pool of 10, a Might Edge of 1, and an Effort "
                      "of 2 (approximately equal to the strength of a fit, capable, adult human), and you can use it "
                      "to move metal objects, push against metal objects, and so on. For example, in your round, you "
                      "could lift and pull a light metal object anywhere within range to yourself or move a heavy "
                      "object (like a piece of furniture) about 10 feet (3 m). This power lacks the fine control to "
                      "wield a weapon or move objects with much speed, so in most situations, it’s not a means of "
                      "attack. You can’t use this ability on your own body. The power lasts for one hour or until its "
                      "Might Pool is depleted, whichever comes first. Action."},
            '2': {
                "Repel Metal":
                    "By manipulating magnetism, you are trained in Speed defense tasks against any incoming attack "
                    "that uses metal. Enabler."
            },
            '3': {
                "CHOICE": {
                    "Destroy Metal":
                        "(3 Intellect points). You instantly tear, rip, or burst a metal object that is within sight, "
                        "within short range, and no bigger than half your size. Attempt an Intellect task to destroy "
                        "the object; the task is eased by three steps compared to breaking it with brute strength. "
                        "Action.",
                    "Guide Bolt":
                        "(4+ Intellect points). When you make an attack with a metallic bolt or metal-tipped arrow on "
                        "a target within short range,  you can improve the attack’s aim and velocity, which grants an "
                        "asset to the attack and inflicts an additional 2 points of damage. If you apply a level of "
                        "Effort, you grant the same benefits to a ranged attack made by an ally within immediate "
                        "range. In any case, you can use this ability only once per round. Enabler."
                }
            },
            '4': {
                "Magnetic Field":
                    "(4 Intellect points). When you wish it, a field of magnetism around you pulls incoming, ranged, "
                    "metallic projectile attacks (such as arrows, bullets, a thrown metal knife, and so on) to the "
                    "ground. You are immune to such attacks for one round. You must be aware of an attack to foil it. "
                    "Enabler."
            },
            '5': {
                "Command Metal":
                    "(5 Intellect points). You reshape a metallic item as you desire. The item must be within sight "
                    "and within short range, and its mass can be no greater than your own. You can affect multiple "
                    "items at once as long as their combined mass falls within these limits. You can fuse multiple "
                    "items together. You can use this power to destroy a metal object (as the Destroy Metal ability), "
                    "or you can craft it into another desired shape (crudely, unless you have the proper crafting "
                    "skills). You can then move the new object anywhere within range. For example, you could take a "
                    "few metal shields, fuse them together, and use the resulting shape to block a doorway. You can "
                    "use this ability to make an attack— causing a foe’s armor to constrict, rendering a metal item "
                    "into shards that you fling across the battlefield, and so on—against one target within short "
                    "range. Regardless of the form of the attack, it is an Intellect action that deals 7 points of "
                    "damage. Action."
            },
            '6': {
                "CHOICE": {
                    "Diamagnetism":
                        "You magnetize any nonmetallic object within short range so that it can be affected by your "
                        "other powers. Thus, with Move Metal, you can move any object. With Repel Metal, you are "
                        "trained in all Speed defense tasks, regardless of whether the incoming attack uses metal. "
                        "And so on. Enabler.",
                    "Iron Punch":
                        "(5+ Intellect points). You pick up a heavy object within short range and hurl it at someone "
                        "within short range, an Intellect action that deals 6 points of damage to the target and to "
                        "the hurled object. For each additional level of Effort applied, you can pick up a slightly "
                        "larger object, allowing you to affect one additional target within short range as long as it "
                        "is next to the prior target. Action."
                }
            }
        }
    },
    "Entertains": {
        "Description": "You are an entertainer: a singer, dancer, poet, storyteller, or something similar. You "
                       "perform for the benefit of others. Naturally charismatic and talented, you have also studied "
                       "to master your art. You know all the old poems, songs, jokes, and stories, and you’re "
                       "skilled at creating new ones, too.",
        "Connection": [
            "Pick one other PC. This character is your worst critic. Your abilities to help or inspire others don’t "
            "function for them.",
            "Pick one other PC. They seem to really enjoy your attempts to entertain, and this brings out the "
            "performer in you. It’s up to that character whether their appreciation is real or they’re just being "
            "polite.",
            "Pick one other PC. They are so inspired and put at ease by your stories or other forms of "
            "entertainment that when you use Levity, they gain +2 to their recovery rolls (instead of +1).",
            "Pick one other PC. This person knows the secret to one of your favorite forms of entertainment. You "
            "worry constantly that they will steal it or reveal it."
        ],
        "Additional Equipment": ["A Musical Instrument or other tools to perform"],
        "Core Features": {},
        "Major Effect Suggestions": "You enchant the target, who remains enchanted as long as you focus all your "
                                    "attention on keeping them that way.",
        "Minor Effect Suggestions": "The target is forever favorably disposed toward you.",
        "Tiers": {
            '1': {
                "Levity":
                    "Through wit, charm, humor, and grace, you are trained in all social interactions other than "
                    "those involving coercion or intimidation. During rests, you put friends and comrades at ease "
                    "so much that they gain +1 to their recovery rolls. Enabler."
            },
            '2': {
                "Inspiration":
                    "Through stories, songs, art, or other forms of entertainment, you inspire your friends. After "
                    "spending 28 hours with you, once per day each of your friends can ease a task. This benefit is "
                    "ongoing while you remain in the friend’s company. It ends if you leave, but it resumes if you "
                    "return to the friend’s company within 28 hours. If you leave the friend’s company for more than "
                    "28 hours, you must spend another 28 hours together to reactivate the benefit. Enabler."
            },
            '3': {
                "CHOICE": {
                    "Knowledge": "Your stories and songs contain truth. You are trained in two areas of knowledge of "
                                 "your choice. Enabler.",
                    "Multitalented": "Being well versed in how to entertain others is reflected in your growing "
                                     "capabilities. You gain 6 new points to divide among your stat Pools however you "
                                     "wish. Enabler."
                }
            },
            '4': {
                "Calm":
                    "(3 Intellect points). Through jokes, song, or other art, you prevent a living foe from attacking "
                    "anyone or anything for one round. Action."
            },
            '5': {"Able Assistance": "When you help someone with a task and they apply a level of Effort, they get a "
                                     "free level of Effort on that task. Enabler."},
            '6': {
                "CHOICE": {
                    "Master Entertainer":
                        "Your Inspiration ability works more effectively, easing your friends’ tasks by two steps "
                        "rather than one step. Enabler.",
                    "Vindictive Performance":
                        "(5 Intellect points). When you tell a joke, perform a song or poem, draw a picture, relate "
                        "an anecdote, or otherwise provide entertainment, you can select one individual from the "
                        "audience who is able to understand you. During your performance, you heap indirect but "
                        "biting derision on this target. If you succeed, the target doesn’t realize that they’ve "
                        "become the victim of your performance until you wrap up the entertainment at a moment you "
                        "choose in a way that strikes home. The target suffers 6 points of Intellect damage (ignores "
                        "Armor) and loses their next turn. One or more actions to initiate."
                }
            }
        }
    },
    "Exists Partially Out of Phase": {
        "Description": "You have the ability to change your phase state. In fact, you’re always slightly out of phase, "
                       "giving you a ghostly translucence. With concentration, you can pass your hand through a solid "
                       "object, allow a solid object to pass harmlessly through you, or literally walk through walls. "
                       "However, moving in and out of different phase states requires extreme force of will and can "
                       "be mentally taxing. The explanation for your strange power lies within some aspect of the "
                       "numenera. Perhaps the ability emerged through the use of (or exposure to) lingering "
                       "transdimensional technology or as the result of an encounter with a creature not native to "
                       "this world or dimension. Perhaps one of your ancestors first developed the power and passed it "
                       "down through generations.",
        "Connection": [
            "Pick one other PC. You have known that character for a while, and they helped you gain control of "
            "your phase states.",
            "Pick one other PC. Sometime in this character’s past, they had a devastating experience with going out "
            "of phase. Whether they choose to tell you about it is up to them.",
            "Pick one other PC. You once accidentally moved your hand right through them. It was an unnerving "
            "experience for you both.",
            "Pick two other PCs. They both really want to go out of phase and have been pestering you about it. But "
            "you’re not convinced they even know what that phrase means."
        ],
        "Additional Equipment": [],
        "Core Features": {},
        "Major Effect Suggestions": "While out of phase, you are also invisible.",
        "Minor Effect Suggestions": "While out of phase, you also have an asset to your Speed defense tasks.",
        "Tiers": {
            '1': {
                "Walk Through Walls":
                    "(2 Intellect points). You can slowly pass through physical barriers at a rate of 1 inch (2.5 cm) "
                    "per round (minimum of one round to pass through any barrier). You can’t act (other than moving) "
                    "or perceive anything until you pass entirely through the barrier. You can’t pass through energy "
                    "barriers. Action."
            },
            '2': {
                "Defensive Phasing":
                    "(2 Intellect points). You can change your phase so that some attacks pass through you harmlessly. "
                    "For the next ten minutes, you gain an asset to your Speed defense tasks, but during this time "
                    "you lose any benefit from armor you wear. Action to initiate."
            },
            '3': {
                "CHOICE": {
                    "Phased Attack":
                        "(3 Intellect points). The attack you make on this turn ignores your foe's armor. The ability "
                        "works for whatever kind of attack you use (melee, ranged, energy, and so on). Enabler.",
                    "Phase Door":
                        "(4 Intellect points). You can phase into a solid object’s surface and then phase out of any "
                        "other solid object within long range of the first, even if the two objects are not connected. "
                        "There must not be any intervening barriers between the two objects, and you must be aware of "
                        "or able to see the destination object. Action."
                }
            },
            '4': {
                "Ghost": "(4 Intellect points). For the next ten minutes, you gain an asset to sneaking tasks. During "
                         "this time, you can move through solid barriers (but not energy barriers) at a rate of 1 foot "
                         "(30 cm) per round, and you can perceive while phased within a barrier or object, which "
                         "allows you to peek through walls. Action to initiate."
            },
            '5': {"Untouchable":
                      "(6 Intellect points). You change your phase state for the next minute so that you can’t affect "
                      "or be affected by normal matter or energy. Only mental attacks and special transdimensional "
                      "energies, devices, orabilities can affect you, but likewise you can’t attack, touch, or "
                      "otherwise affect anything. Action to initiate."},
            '6': {"CHOICE": {
                "Enhanced Phased Attack":
                    "(5 Intellect points). This ability works like the third-tier Phased Attack ability except that "
                    "your attack also disrupts the foe’s vitals, dealing an additional 5 points of damage. Enabler.",
                "Phase Foe":
                    "(6+ Intellect points). You gather disrupting energy in your fingertip and touch a creature. If "
                    "the target is an NPC or a creature of level 3 or lower, it becomes phased as if it had used your "
                    "Ghost ability. However, unless it can figure out how to control its movement while being phased, "
                    "which most creatures have no experience with, it begins to sink through solid matter. If it can’t "
                    "control itself or end the effect, it might be gone for good because when it becomes solid again "
                    "after ten minutes, it’s probably deep in the earth. For each additional level of Effort you "
                    "apply, you can attempt to affect a target of one level higher. Action."
            }}
        }
    },
    "Explores Dark Places": {
        "Description": "You explore the foreboding ruins and mysterious locales of the ancient eras, trained in such "
                       "activities by those who have gone before you. You’re the archetypical treasure hunter, "
                       "scavenger, and finder of lost things. You spend so much of your time in the dark that you "
                       "slowly adapt to it, almost becoming a creature of the gloom yourself. Even in civilized areas, "
                       "you prefer to keep to the shadows.",
        "Connection": [
            "Pick one other PC. This character was your companion on previous expeditions, and the two of you work "
            "so well together that you both gain an asset to any die rolls to collaborate on the same task, fight the "
            "same foe, and so on.",
            "Pick two other PCs. You think you once saw them through a keyhole doing something illegal. You can "
            "choose whether or not to share that information. The characters can choose whether it was really them "
            "(it could have been neither, one, or both), and they may or may not share that information in return.",
            "Pick one other PC. This person always seems to hear you, no matter how stealthy you try to be.",
            "Pick one other PC. This character is so loud in everything they do that you feel obligated to try to "
            "help them learn to move more quietly through the world. Whether or not they’re interested is up to them."
        ],
        "Additional Equipment": ["Explorer's pack"],
        "Core Features": {"Darkness Powers":
                              "Your special abilities (such as Nano esoteries) make almost no sound, and whatever "
                              "visual displays they produce are dark and shadowy. These alterations change nothing "
                              "other than the appearance of the effects. A Flash esotery is a silent burst of shadows, "
                              "a Barrier esotery is a mass of shadowy wisps, and so on."},
        "Major Effect Suggestions": "The target is also stunned and loses its next turn.",
        "Minor Effect Suggestions": "The target is also dazed for one round, during which time all of its tasks "
                                    "are hindered.",
        "Tiers": {
            '1': {"Superb Explorer": "You are trained in searching, listening, climbing, balancing, and jumping "
                                     "tasks. Enabler."},
            '2': {
                "Superb Infiltrator": "You are trained in lockpicking and tinkering with devices in an effort to make "
                                      "them work, or at least work for you. Enabler.",
                "Eyes Adjusted": "You can see in extremely dim light as though it were bright light. You can see in "
                                 "total darkness as if it were extremely dim. Enabler."
            },
            '3': {"CHOICE": {
                "Nightstrike": "When you attack a foe in dim light or darkness, you get a free level of Effort on "
                               "the attack. Enabler.",
                "Slippery Customer": "When you apply Effort to tasks involving escaping from bonds, fitting in tight "
                                     "spaces, and other contortionist tasks, you get a free level of Effort on the "
                                     "task. Thanks to your experience, you are also trained in Speed defense tasks "
                                     "while wearing light armor or no armor. Enabler."
            }},
            '4': {
                "Resilient": "In your explorations of dark places, you’ve been exposed to all sorts of terrible "
                             "things and are developing a general resistance. You gain +1 to Armor and are trained "
                             "in Might defense tasks. Enabler."
            },
            '5': {"Dark Explorer": "You ignore penalties for any action (including fighting) in extremely dim light "
                                   "or in cramped spaces. Combined with your Eyes Adjusted ability, you can act "
                                   "without penalty even in total darkness. You are trained in sneaking tasks while "
                                   "in dim or no light. Enabler."},
            '6': {"CHOICE": {
                "Blinding Attack":
                    "(3 Speed points). If you have a source of light, you can use it to make a melee attack against "
                    "a target. If successful, the attack deals no damage, but the target is blinded for one "
                    "minute. Action.",
                "Embraced by Darkness":
                    "(6 Intellect points). For the next hour, you take on some characteristics of a shadow thanks to "
                    "a fundamental adaptation of your flesh or a device you’ve kept secret. Your appearance is a "
                    "dark silhouette. When you apply a level of Effort to sneaking tasks, you get a free level of "
                    "Effort on the task. During this time, you can move through the air at a rate of a short distance "
                    "per round, and you can move through solid barriers (even those that are sealed to prevent the "
                    "passage of light or shadow), but not energy barriers, at a rate of 1 foot (30 cm) per round. "
                    "You can perceive while passing through a barrier or object, which allows you to peek through "
                    "walls. As a shadow, you can’t affect or be affected by normal matter. Likewise, you can’t attack, "
                    "touch, or otherwise affect anything. However, attacks and effects that rely on light can affect "
                    "you, and sudden bursts of light can potentially make you lose your next turn. Action to initiate."
            }}
        }
    },
    "Fights with Panache": {
        "Description": "You know that style is at least as important as substance. Defeating foes is secondary to "
                       "looking good while doing it. Some might call you a swashbuckler or daredevil. You leap through "
                       "the air, make a flourish with your weapon, and attack, usually with a clever, biting show of "
                       "wit. Your enemies hate you, but your allies adore you. Just watching you fight is "
                       "entertaining.",
        "Connection": [
            "Pick one other PC. You’re always trying to impress this character with your skill, wit, appearance, or "
            "bravado. Perhaps they are a rival, perhaps you need their respect, or perhaps you’re romantically "
            "interested in them.",
            "Pick one other PC. This character seems to anticipate your next move almost before you even begin it. "
            "When they collaborate with you on the same task or fight the same foe, you gain an asset on the task.",
            "Pick one other PC. You fear that the character is jealous of your abilities and worry that it might "
            "lead to problems.",
            "Pick one other PC. This character is so enamored of your swashbuckling, entertaining ways during combat "
            "that they sometimes forget to take their own action."
        ],
        "Additional Equipment": ["Extremely Stylish Clothes", "A Jeweled Weapon"],
        "Core Features": {},
        "Major Effect Suggestions": "Make an additional attack with your weapon on your turn.",
        "Minor Effect Suggestions": "The target is so dazzled by your style that it is dazed for one round, during "
                                    "which time all of its tasks are hindered.",
        "Tiers": {
            '1': {
                "Attack Flourish":
                    'With your attack, you add stylish moves, entertaining quips, or a certain "something" that '
                    'entertains or impresses others. One creature you choose within short range who can see you gains '
                    'an asset to its next task if taken within a round or two. Enabler.'
            },
            '2': {
                "Quick Block": "If you use a light or medium weapon, you are trained in Speed defense tasks. Enabler."
            },
            '3': {"CHOICE": {
                "Acrobatic Attack":
                    "(1+ Speed points). You leap into the attack, twisting or flipping through the air. If you roll a "
                    "natural 17 or 18, you can choose to have a minor effect rather than deal extra damage. If you "
                    "apply Effort to the attack, you get a free level of Effort on the task. You can’t use this "
                    "ability if your Speed is reduced from wearing armor. Enabler.",
                "Flamboyant Boast":
                    "(1 Intellect point). You boastfully describe an act that you will accomplish, and then as part "
                    "of the same action, you attempt it. If an average person would find the action difficult "
                    "(or impossible) and you succeed on it, creatures who witnessed it who are not your allies are "
                    "potentially dazed on their next turn, and all tasks they attempt are hindered. The GM will help "
                    "you determine whether your boast is something that would impress onlookers so significantly. If "
                    "you attempt the task you boast about but fail to accomplish it, all your attempts to affect or "
                    "attack onlookers who saw you are hindered for about ten minutes. Enabler."
            }},
            '4': {
                "Mobile Fighter":
                    "(3 Speed points). As part of your attack, you can leap on or over obstacles, swing from ropes, "
                    "run along narrow surfaces, or otherwise move around the battlefield at your normal speed as if "
                    "such tasks were routine (difficulty 0). You can’t use this ability if your Speed is reduced "
                    "from wearing armor. Enabler."
            },
            '5': {
                "Block for Another":
                    "If you use a light or medium weapon, you can block attacks made against an ally "
                    "near you. Choose one creature within immediate range. You provide an asset to that creature’s "
                    "Speed defense tasks. You can’t use Quick Block while using Block for Another. Enabler."
            },
            '6': {"CHOICE": {
                "Agile Wit":
                    "When attempting a Speed task, you instead can roll (and spend points) as if it were an Intellect "
                    "action. If you apply Effort to this task, you can spend points from your Intellect Pool instead "
                    "of your Speed Pool (in which case you also use your Intellect Edge instead of your Speed Edge). "
                    "Enabler.",
                "Return to Sender":
                    "(3 Speed points). If you succeed at a Speed defense task against a melee attack, you can make an "
                    "immediate melee attack against your foe. You can use this ability only once per round. Enabler."
            }}
        }
    },
    "Focuses Mind Over Matter": {
        "Description": "Telekinesis. Psychokinesis. Mind over matter. The power has many names, but in the end, it "
                       "all boils down to one thing—the molecules that make up all matter are yours to command. You "
                       "likely call yourself a telekinetic or just a TK.",
        "Connection": [
            "Pick one other PC. This character can cause your telekinetic powers to act oddly. Every once in a while, "
            "if the character stands directly next to you, your powers are canceled, but at other times, they seem "
            "improved when used near the PC.",
            "Pick one other PC. This person thinks that your powers are completely hypothetical.",
            "Pick one other PC. You once joked that you could read their mind. Whether they found that exciting or "
            "utterly terrifying is up to them.",
            "Pick one other PC. You feel strangely protective of that character and plan to do your best to keep "
            "them from harm."
        ],
        "Additional Equipment": [],
        "Core Features": {
            "Mental Powers": "Your special abilities that would normally use force or other energy instead use "
                             "psychokinetic force. For example, a Flash or an Onslaught force blast is a psychokinetic "
                             "blast from your mind. This alteration changes nothing except that you don’t need a free "
                             "hand to perform those abilities. In addition, you can choose to learn Impetus instead of "
                             "one of the abilities granted by your type. Enabler.",
            "ADDITIONAL ABILITIY CHOICE": {
                "Impetus":
                    "(2 Intellect points): A loose object within short range that you could carry in one hand is "
                    "drawn to your free hand. If the object is stuck or held by another creature, you must succeed on "
                    "a Might roll to rip it free, or the object remains where it was. Action."
            }
        },
        "Major Effect Suggestions": "You can move or affect twice as much as normal.",
        "Minor Effect Suggestions": "An object moves faster or more efficiently.",
        "Tiers": {
            '1': {
                "Deflect Attacks":
                    "(1 Intellect point). Using your mind, you protect yourself from incoming attacks. For the next "
                    "ten minutes, you are trained in Speed defense tasks. Action to initiate."
                  },
            '2': {
                "Telekinesis":
                    "(2 Intellect points). You can exert force on objects within short range. Once activated, your "
                    "power has an effective Might Pool of 10, a Might Edge of 1, and an Effort of 2 (approximately "
                    "equal to the strength of a fit, capable, adult human), and you can use it to move objects, push "
                    "against objects, and so on. For example, you could lift and pull a light object anywhere within "
                    "range to yourself or move a heavy object (like a piece of furniture) about 10 feet (3 m). This "
                    "power lacks the fine control to wield a weapon or move objects with much speed, so in most "
                    "situations, it’s not a means of attack. You can’t use this ability on your own body. The power "
                    "lasts for one hour or until its Might Pool is depleted, whichever comes first. Action."
            },
            '3': {"CHOICE":{
                "Cloak of Opportunity":
                    "(5 Intellect points). You set small objects from the environment (rocks, broken cyphers, clumps "
                    "of drit, and so on) swirling about you for up to ten minutes, which grants you +2 Armor. "
                    "Action to initiate.",
                "Enhance Strength":
                    "(3 Intellect points). For the next ten minutes, you gain an asset on tasks that depend on brute "
                    "force, such as moving a heavy object, smashing down a door, or hitting someone with a melee "
                    "weapon. Action to initiate.",
            }},
            '4': {
                "Apportation":
                    "(4 Intellect points). You call a physical object to you. You can choose any piece of normal "
                    "equipment on the standard equipment list, or (no more than once per day) you can allow the GM to "
                    "determine the object randomly. If you call a random object, it has a 10 percent chance of being "
                    "a cypher or artifact, a 10 percent chance of being an oddity, a 40 percent chance of being a "
                    "piece of standard equipment, and a 40 percent chance of being a bit of worthless junk. You can’t "
                    "use this ability to take an item held by another creature. Action."
            },
            '5': {
                "Psychokinetic Attack":
                    "(5 Intellect points). You can use this attack in one of two ways. The first is to pick up a "
                    "heavy object and hurl it at someone within short range. This attack is an Intellect action, and "
                    "if successful, it deals 6 points of damage to the target and to the hurled object (which could "
                    "be another foe, although that would require two rolls—one roll to grab the first foe and another "
                    "roll to hit the second foe with the first). The second way is to unleash a shattering burst of "
                    "power that works only against an inanimate object no larger than half your size. Make an "
                    "Intellect roll to instantly destroy the object; the task is eased by three steps compared to "
                    "breaking it with brute strength. Action."
            },
            '6': {"CHOICE": {
                "Improved Apportation":
                    "(6 Intellect points). You call a creature of up to level 3, which appears next to you. You can "
                    "choose a creature that you’ve previously encountered, or (no more than once per day) you can "
                    "allow the GM to determine the creature randomly. If you call a random creature, it has a 10 "
                    "percent chance of being a creature of up to level 5. The creature has no memory of anything "
                    "before being called by you, though it can speak and has the general knowledge a creature of its "
                    "type should possess. The creature is receptive to communication and helping you (unless shown "
                    "that it should do otherwise). Action.",
                "Reshape Matter":
                    "(6 Intellect points). Your mastery of telekinesis is so great that you can reshape objects on "
                    "a molecular level. You can affect a single object no larger than you, and the object must be "
                    "visible and close enough for you to touch. You can use this ability to damage the object (as if "
                    "using Psychokinetic Attack, except the task is eased by four steps instead of three), or you can "
                    "attempt a crafting task to reshape the object into another form. Reshaping an object usually has "
                    "a difficulty equal to 1 plus the level of the finished object."
            }}
        }
    },
    "Fuses Flesh and Steel": {
        "Description": "At some point in your past, some of your organic parts were replaced with artificial "
                       "components. (Alternatively, you belong to a secret species of biomechanical hybrids.) These "
                       "artificial components might be subdermal, or they might resemble more overt metal or synth "
                       "plating on your skin. They can also take the form of threadlike tendrils of circuitry winding "
                       "across your flesh. Whatever their appearance, these components give you special abilities. "
                       "As you advance, you can add to, modify, or discover new functions for them. Unfortunately, "
                       "your artificial body also has special requirements when it takes damage.",
        "Connection": [
            "Pick one other PC. This character knows your true nature, even if no one else does. If your components "
            "are not particularly hidden, they know a different secret of yours, such as a preprogrammed word that "
            "will shut you down for ten minutes.",
            "Pick one other PC. Being close to this person sometimes makes your mechanical parts vibrate slightly. "
            "You can decide whether this sensation is unnerving or pleasant.",
            "Pick one other PC. You’re pretty sure that this character is just here to mine you for parts. They "
            "choose whether or not this is true.",
            "Pick one other PC who also has mechanical parts. The two of you have bonded over conversations about "
            "this element you share, and you feel a special connection."
        ],
        "Additional Equipment": ["A bag of light tools", "A variety of parts to repair yourself"],
        "Core Features": {},
        "Major Effect Suggestions": "You discharge a small pulse of power into your foe. Make an immediate attack "
                                    "against that foe (using the same stat as the action that caused the major "
                                    "effect). If the attack succeeds, it deals 4 points of electrical damage.",
        "Minor Effect Suggestions": "Your servos learn from your successful actions. You gain an asset to similar "
                                    "actions involving the same task (such as making attacks against the same foe or "
                                    "operating the same device).",
        "Tiers": {
            '1': {
                "Enhanced Body": "You gain +1 to Armor, +3 to your Might Pool, and +3 to your Speed Pool. Enabler.",
                "Special Healing":
                    "Traditional healing skills, medicines, and techniques work only half as well for you. Each time "
                    "you start at full health, the first 5 points of damage you take can never be healed in these "
                    "ways or recovered normally. Instead, you must use repairing skills and abilities to restore "
                    "those points. For example, if you start with a full Might Pool of 10 and take 8 points of "
                    "damage, you can use recovery rolls to restore 3 points, but the remaining 5 points must be "
                    "restored with repair tasks."
            },
            '2': {
                "Interface": "By directly plugging into a device, you can identify and learn to operate it as though "
                             "the task were 1 level lower. Enabler."
            },
            '3': {"CHOICE":{
                "Sensing Package":
                    "You can see in dim light and darkness as if it were bright light, and you can see up to a short "
                    "distance through fog, smoke, and other obscuring phenomena. In addition, if you apply a level "
                    "of Effort to perception or searching tasks, you get a free level of Effort on that task. Enabler.",
                "Weaponization":
                    "One light or medium melee weapon of your choice is built into your body, and you are trained in "
                    "using it. The weapon is concealed until you wish to use it. Enabler."
            }},
            '4': {
                "Fusion":
                    "You can fuse your cyphers and artifacts with your body. These fused devices function as if they "
                    "were 1 level higher. Enabler."
            },
            '5': {
                "Deep Reserves":
                    "Once each day, you can transfer up to 5 points between your Pools in any combination, at a rate "
                    "of 1 point per round. For example, you could transfer 3 points of Might to Speed and 2 points "
                    "of Intellect to Speed, which would take a total of five rounds. Action."
            },
            '6': {"CHOICE":{
                "Power Surge": "In addition to your normal recovery rolls each day, you can—at any time between "
                               "ten-hour rests—recover 1d6 + 6 points to your Intellect Pool. Action.",
                "Ultra Enhancement": "You gain +1 to Armor and +5 to each of your three stat Pools. Enabler."
            }}
        }
    },
    "Howls at the Moon": {
        "Description": "Sometimes the numenera is a double-edged sword. You are cursed and blessed to be able to "
                       "transform into a powerful creature, drawing additional mass from a transdimensional source. "
                       "You and the GM should work out the exact nature of the creature, including its appearance, "
                       "but it’s a wild beast of rage and blood—at least until you learn to control it. Creatures like "
                       "you are often called “lycanthropes.”",
        "Connection": [
            "Pick one other PC. That character is able to soothe you when you’re in beast form. You’ll never attack "
            "them while transformed, and if they spend three consecutive turns using their action to calm you down, "
            "you can revert to your normal form without having to make a roll.",
            "Pick one other PC. You believe that this character intends to convince you to join an entertainment "
            "venue (or capture you for the same). They choose whether or not this is true.",
            "Pick two other PCs. They know that it’s beneficial for you to kill and eat a creature while you’re in "
            "beast form, and they often work together to make sure that happens.",
            "Pick one other PC. Since this character saw you in beast form, they have been terrified of you. You are "
            "determined to show them that you’re not as dangerous as they believe.",
        ],
        "Additional Equipment": ["an accurate chronometer artifact that always lets you know when the next "
                                 "transformation is coming."],
        "Core Features": {},
        "Major Effect Suggestions": "Your attack conveys a small bit of your lycanthropy. If your foe survives, one "
                                    "month later, the target transforms into an uncontrolled beast. The GM decides "
                                    "what happens from there.",
        "Minor Effect Suggestions": "The target is so intimidated by your bestial attack that it is dazed for one "
                                    "round, hindering its tasks.",
        "Tiers": {
            '1': {
                "Beast Form":
                    "On five consecutive nights each month, you change into a monstrous beast for up to one hour "
                    "each night. In this new form, you gain +8 to your Might Pool, +1 to your Might Edge, +2 to "
                    "your Speed Pool, and +1 to your Speed Edge. While in beast form, you can’t spend Intellect "
                    "points for any reason other than to try to change to your normal form before the one-hour "
                    "duration is over (a difficulty 2 task). In addition, you attack any and every living creature "
                    "within short range. After you revert to your normal form, you take a –1 penalty to all rolls for "
                    "one hour. If you did not kill and eat at least one substantial creature while in beast form, the "
                    "penalty increases to –2 and affects all your rolls for the next 28 hours. Action to change back."
            },
            '2': {
                "Controlled Change":
                    "You can try to change into your beast form on any night you wish (a difficulty 3 Intellect task). "
                    "Any transformations you make using this power are in addition to the five nights per month that "
                    "you change involuntarily. Action to change.",
            },
            '3': {"CHOICE": {
                "Bigger":
                    "Your beast form grows bigger than before, during which time you achieve a height of 12 feet "
                    "(4 m). Being so large, your beast form gains the following additional bonuses: +1 to Armor, "
                    "+5 to your Might Pool, and you are trained in using your fists as heavy weapons (if you weren’t "
                    "already). However, your Speed defense tasks are hindered. While bigger, you also gain an asset "
                    "to tasks that are easier for a larger creature to perform, like climbing, intimidating, wading "
                    "rivers, and so on. Enabler.",
                "Greater Beast Form":
                    "Your beast form gains the following additional bonuses: +1 to your Might Edge, +2 to your "
                    "Speed Pool, and +1 to your Speed Edge. Enabler.",
            }},
            '4': {
                "Greater Controlled Change":
                    "It’s easier to change into and out of your beast form. Transforming either way is now a "
                    "difficulty 2 Intellect task. Enabler."
            },
            '5': {
                "Enhanced Beast Form":
                    "Your beast form gains the following additional bonuses: +3 to your Might Pool, +2 to your Speed "
                    "Pool, and +2 to Armor. Enabler."
            },
            '6': {"CHOICE":{
                "Lethal": "When you attack in your beast form, you inflict +5 points of damage. Enabler.",
                "Perfect Control":
                    "You no longer need to make a roll to change into your beast form or your normal form. You can "
                    "change back and forth as your action. When you return to your normal form, you no longer take a "
                    "penalty to your rolls. Enabler."
            }}
        }},
    "Hunts": {
        "Description": "You are a tracker. Perhaps you hunt animals or more deadly creatures. Perhaps you go after "
                       "people as a bounty hunter, law enforcer, or killer for hire. Whatever form your hunting takes, "
                       "you are trained in stalking your quarry and bringing it down. You are a dangerous individual.",
        "Connection": [
            "Pick one other PC. That person once saw you show surprising mercy toward your prey, and now you hope "
            "they keep it quiet—it might harm your reputation.",
            "Pick one other PC. You accidentally caught them in one of your traps, and they had to get free.",
            "Pick one other PC. Back in your bounty hunter days (which may or may not be over), you were hired to "
            "track down someone who was close to this character.",
            "Pick one other PC. You’ve noticed that it’s almost impossible to track this character, but you’re "
            "determined to figure out a way."
        ],
        "Additional Equipment": [
            "Boots that muffle your footsteps, giving you an asset on any roll made involving sneaky movement."
        ],
        "Core Features": {},
        "Major Effect Suggestions": "Your foe pauses, terrified by your prowess, and takes no action on their turn.",
        "Minor Effect Suggestions": "You can attempt an intimidating task to cause your foe to immediately surrender.",
        "Tiers": {
            '1': {
                "Tracker": "You are trained in following and identifying tracks. Enabler.",
                "Stalker": "You gain an asset to all types of movement tasks (including climbing, swimming, jumping, "
                           "and balancing). Enabler."
            },
            '2': {
                "Sneak": "You ease stealth and initiative tasks. Enabler.",
                "Quarry": "(2 Intellect points). Choose a quarry (a single individual creature that you can see). You "
                          "are trained in all tasks involving following, understanding, interacting with, or fighting "
                          "that creature. You can have only one quarry at a time. Action to initiate."
            },
            '3': {"CHOICE":{
                "Horde Fighting":
                    "When two or more foes attack you at once in melee, you can use them against each other. You "
                    "are trained in either Speed defense rolls or attack rolls (your choice) against them. Enabler.",
                "Sprint and Grab":
                    "(2 Speed points). You can run a short distance and make a melee attack to grab a foe of your size "
                    "or smaller. A successful attack means you grab the foe and bring it to a halt if it was moving "
                    "(this can be treated as a tackle, if appropriate). Action."
            }},
            '4': {
                "Surprise Attack":
                    "If attacking from a hidden vantage, with surprise, or before your opponent has acted, you get a "
                    "free level of Effort on the attack. On a successful hit, you inflict 2 additional points of "
                    "damage. Enabler."
            },
            '5': {
                "Hunter’s Drive":
                    "(5 Intellect points) Through force of will, when you wish it, you grant yourself greater "
                    "prowess in the hunt for ten minutes. During this time, you gain an asset to all tasks involving "
                    "your quarry, including attacks. Your quarry is the creature you selected with your second-tier "
                    "ability. Enabler."
            },
            '6': {"CHOICE":{
                "Master Combatant":
                    "Choose one type of attack in which you are already trained: light bashing, light bladed, light "
                    "ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or heavy "
                    "ranged. You are specialized in attacks using that type of weapon. Enabler.",
                "Multiple Quarry":
                    "(6 Intellect points). This ability functions like the second-tier Quarry ability except that you "
                    "can select up to three creatures as quarry. You must be able to see all three creatures when "
                    "you initiate this ability. Your Hunter’s Drive ability applies to all three creatures. Action "
                    "to initiate."
            }}
        }},
    "Lives in the Wilderness": {
        "Description": "You dwell in the wilds. You probably have done so most, if not all, of your life, coming to "
                       "understand the mysteries of nature, weather, and survival. The ways of flora and fauna are "
                       "your ways.",
        "Connection": [
            "Pick one other PC who isn’t from the wilderness. You can’t help but feel a little contempt for that "
            "character and their “civilized” ways, which show disdain for all things natural and (to your mind) true.",
            "Pick one other PC. This character is one of the few people that you are completely comfortable around, "
            "and you are often surprised at how easily you let down your guard near them.",
            "Pick one other PC. This character once saved you from an uncomfortable social situation, and you still "
            "feel grateful.",
            "Pick one other PC. This person seems to understand civilization in the same way that you understand the "
            "wilderness. You could choose to help each other or despise each other for this different way of seeing "
            "the world."
        ],
        "Additional Equipment": ["a directional compass."],
        "Core Features": {},
        "Major Effect Suggestions": "A foe that is a natural creature becomes warily passive.",
        "Minor Effect Suggestions": "A foe that is a natural creature flees rather than continue to fight you.",
        "Tiers": {
            '1': {
                "Wilderness Life":
                    "You are trained in two of the following: climbing, swimming, navigation, or identifying plants "
                    "and creatures. Enabler.",
                "Wild Hardiness":
                    "You gain 3 points to your Might Pool. Enabler.",
            },
            '2': {
                "Living off the Land":
                    "Given an hour or so, you can always find edible food and potable water in the wilderness. You "
                    "can even find enough for a small group of people, if need be. Further, since you’re so hardy and "
                    "have gained resistance over time, you are trained in resisting the effects of natural poisons "
                    "(such as those from plants or living creatures). You’re also immune to natural diseases. Enabler.",
                "Wilderness Explorer":
                    "While taking any action (including fighting) in the wild, you ignore any penalties due to natural "
                    "causes such as tall grass, thick brush, rugged terrain, weather, and so on. Enabler."
            },
            '3': {"CHOICE": {
                "Animal Senses and Sensibilities":
                    "You are trained in listening and spotting things. In addition, most of the time, the GM should "
                    "alert you if you’re about to walk into an ambush or a trap that is lower than level 5. Enabler.",
                "Wilderness Encouragement":
                    "(3 Intellect points). While in the wilderness, or when talking about your time in the wilderness, "
                    "your stirring words of encouragement grant a target within short range that can understand you "
                    "1d6 points to one Pool. You can’t use this ability on the same creature again until they’ve made "
                    "a recovery roll. Action."
            }},
            '4': {
                "Wilderness Awareness":
                    "(4 Intellect points). Your connection to the natural world extends to a degree that some would "
                    "call supernatural. While in the wilderness, you can extend your senses up to a mile in any "
                    "direction and ask the GM a very simple, general question about that area, such as “Where is the "
                    "margr camp?” or “Is my friend Deithan still alive?” If the answer you seek is not in the area, "
                    "you receive no information. Action."
            },
            '5': {
                "The Wild Is on Your Side":
                    "(5 Intellect points). While you’re in the wilderness, foes within short range are tripped by "
                    "rocks, tangled in vines, bitten by insects, and distracted or confused by small animals, which "
                    "hinders all their tasks for ten minutes. Action to initiate."
            },
            '6': {"CHOICE": {
                "One With the Wild":
                    "(6 Intellect points). For the next hour, natural animals and plants within long range will not "
                    "knowingly harm you or those you designate. In addition, your Might Edge, Speed Edge, and "
                    "Intellect Edge increase by 1, and if you make any recovery rolls during this period, you "
                    "recover twice as many points. Action to initiate.",
                "Wild Camouflage":
                    "(4 Intellect points). By drawing your clothing about you just so and using various tricks and "
                    "your deep knowledge of your surroundings, you become invisible in the wilderness for ten "
                    "minutes. While you are invisible, this asset eases your stealth and Speed defense tasks by two "
                    "steps. This effect ends if you do something to reveal your presence or position—attacking, using "
                    "an ability, moving a large object, and so on. If this occurs, you can regain the remaining "
                    "invisibility effect by taking an action to focus on hiding your position. Action to initiate or "
                    "reinitiate."
            }}
        }
    },
    "Masters Defense": {
        "Description": "Protecting yourself is obviously important in dangerous situations, and you are particularly "
                       "good at it. Cautious and prudent, you learn techniques to defend against all kinds of "
                       "attacks, both physical and mental. The winner is often the last person standing, and you’ve "
                       "done all you can to ensure that person will be you.",
        "Connection": [
            "Pick one other PC. This character protected you from harm recently, and you feel indebted to them for "
            "saving your life.",
            "Pick one other PC. This person thinks you are an incredibly selfish person, perhaps based on their belief "
            "that you always save yourself first.",
            "Pick one other PC. You once fought on opposite sides of a combat.",
            "Pick one other PC. This character seems to be a jinx for you. Whenever they are next to you, your Speed "
            "defense tasks are hindered."
        ],
        "Additional Equipment": ["A Shield"],
        "Core Features": {},
        "Major Effect Suggestions": "If an attack would hit you next round, it harmlessly strikes your shield instead "
                                    "if you choose.",
        "Minor Effect Suggestions": "You gain an asset to Speed defense rolls for one round.",
        "Tiers": {
            '1': {
                "Shield Master":
                    "When you use a shield, in addition to the asset it gives you (easing Speed defense tasks), you "
                    "can act as if you are trained in Speed defense tasks. However, in any round in which you use this "
                    "benefit, your attacks are hindered. Enabler."
            },
            '2': {
                "Sturdy": "You are trained in Might defense tasks. Enabler.",
                "Armor Expert": "When you wear any armor, the Speed cost for wearing it is reduced by 1. Enabler."
            },
            '3': {"CHOICE": {
                "Dodge and Resist":
                    "(3 Speed points). You can reroll any of your Might, Speed, or Intellect defense rolls and take "
                    "the better of the two results. Enabler.",
                "Dodge and Respond":
                    "(3 Might points). If a melee attack misses you, you can immediately make a melee attack in "
                    "return, but no more than once per turn. Enabler."
            }},
            '4': {
                "Tower of Will":
                    "You are trained in Intellect defense tasks and gain +3 points to your Intellect Pool. Enabler.",
                "Armor Master":
                    "You reduce the Speed cost of any armor you wear to 0 (if it isn’t already 0). Enabler."
            },
            '5': {
                "Nothing but Defend":
                    "If you do nothing on your turn but defend, you are specialized in all defense tasks for one "
                    "round. Action."
            },
            '6': {"CHOICE": {
                "Defense Master":
                    "Every time you succeed at a Speed defense task, you can make an immediate attack against your "
                    "foe. (This ability replaces Dodge and Respond, if you took that; you can exchange that ability "
                    "for Dodge and Resist.) Your attack must be the same type (melee weapon, ranged weapon, or "
                    "unarmed) as the attack you defend against. If you don’t have an appropriate type of weapon "
                    "ready, you can’t use this ability. Enabler.",
                "Wear It Well": "When you wear armor of any kind, you gain an additional +1 to Armor. Enabler."
            }}
        }
    },
    "Masters Weaponry": {
        "Description": "You have worked long and hard with one particular type of weapon: bows, swords, axes, "
                       "daggers, whips, or whatever you choose. Thus, you are an archer, a swordsman, an axe master, "
                       "a mistress of knives, or whatever is appropriate to your chosen weapon. A master of the rapier "
                       "is different than a master of the warhammer, and an archer is different than a whip wielder.",
        "Connection": [
            "Pick one other PC. That character shows potential in the use of your weapon. You would like to train "
            "them, but you’re not necessarily qualified to teach (that’s up to you), and they might not be interested "
            "(that’s up to them).",
            "Pick one other PC. If that person is within immediate range when you’re in a fight, sometimes they grant "
            "you an asset, and sometimes they hinder you (50% chance either way, determined per fight).",
            "Pick one other PC. You once saved this person’s life, and they feel indebted to you. You wish they "
            "didn’t; it’s all just part of the job.",
            "Pick one other PC. This person recently mocked your combat stance. How you deal with this (if at all) "
            "is up to you."
        ],
        "Additional Equipment": ["a high-quality weapon of your choosing."],
        "Core Features": {
            "Weaponry Powers":
                "If you have “supernatural” special abilities (such as some esoteries), these look like your chosen "
                "weapon. So the force blast of the Onslaught esotery appears to be a large weapon made of force, and "
                "the Flash esotery produces a flurry of weaponry. These alterations change nothing other than the "
                "appearance of the effects. As another example, Barrier becomes a wall of swirling blades of energy. "
                "This alteration changes the esotery such that it is not a solid barrier but rather inflicts 1 point "
                "of damage to anyone who touches it and 4 points of damage to anyone who passes through it."
        },
        "Major Effect Suggestions": "Make an immediate additional attack with the weapon as part of your turn.",
        "Minor Effect Suggestions": "The target is so dazzled by your expertise that it is dazed for one round, "
                                    "hindering all of its tasks.",
        "Tiers": {
            '1': {
                "Weapon Master": "You gain a +1 bonus to damage with your chosen weapon. Enabler.",
                "Weapon Crafter": "You are trained in crafting tasks associated with your chosen weapon. For "
                                  "instance, if your weapon is a bow, you are trained in tasks related to crafting "
                                  "bows and fletching arrows; if your weapon is a sword, you are trained in tasks for "
                                  "forging swords and sharpening blades; and so on. Enabler."
            },
            '2': {
                "Weapon Defense":
                    "While your chosen weapon is in your hand(s), you are trained in Speed defense rolls. Enabler."
            },
            '3': {"CHOICE": {
                "Disarming Strike":
                    "(3 Speed points) Your attack inflicts 1 point less damage and disarms your foe so that their "
                    "weapon is now 10 feet (3 m) away on the ground. (If your chosen weapon is a whip, you can "
                    "instead deposit the disarmed weapon into your hands; if your chosen weapon is a bow or other "
                    "ranged weapon that fires physical rounds, you can instead “nail” the disarmed weapon to a "
                    "nearby object or structure. Choosing to do either of these hinders your attack.) Action.",
                "Rapid Attack":
                    "(3 Speed points) Once per round, you can make an additional attack with your chosen weapon. "
                    "Enabler."
            }},
            '4': {
                "Never Fumble":
                    "If you roll a natural 1 when attacking with your chosen weapon, you can ignore or countermand the "
                    "GM intrusion for that roll. You can never be disarmed of your chosen weapon, nor will you ever "
                    "drop it accidentally. Enabler."
            },
            '5': {
                "Extreme Mastery":
                    "(6 Might or 6 Speed points). When using your chosen weapon, you can reroll any attack roll you "
                    "wish and take the better of the two results. Enabler."
            },
            '6': {"CHOICE": {
                "Damage Dealer":
                    "You gain a +3 bonus to damage with your chosen weapon. This bonus adds to the one from the "
                    "Weapon Master ability, giving you a total bonus of +4. Enabler.",
                "Death Dealer (5 Might points)":
                    "If you strike a foe of level 3 or less with your chosen weapon, you kill the target instantly. "
                    "Action.",
                "Master Combatant":
                    "Choose one type of attack in which you are already trained: light bashing, light bladed, light "
                    "ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or heavy "
                    "ranged. You are specialized in attacks using that type of weapon. Enabler.",
            }}
        }
    },
    "Murders": {
        "Description": "The murderous assassin is a master of dealing death. No one is better at sneaking into a "
                       "location, eliminating a target, and slipping out again. Obviously, a professional killer is "
                       "not likely to have a lot of friends.",
        "Connection": [
            "Pick one other PC. That character knows your real identity, profession, and background. To all others, "
            "the truth about you is a closely guarded secret.",
            "Pick one other PC. You were recently approached by someone who wanted to hire you to take that character "
            "out. You haven’t yet decided whether to take the job or warn them that their life is in danger.",
            "Pick two other PCs. One night after perhaps too much celebrating, you loudly claimed responsibility for "
            "a murder you didn’t commit. These two characters were the only ones who heard. Whether they believe you "
            "or not is up to them.",
            "Pick one other PC. That character is the one who got you started down the path of taking lives, whether "
            "they know it or not."
        ],
        "Additional Equipment": ["a disguise kit", "three doses of a level 2 blade poison that inflicts 5 points of "
                                                   "damage."],
        "Core Features": {},
        "Major Effect Suggestions": "If you have poison amid your belongings, you were able to apply it just before "
                                    "the strike, adding the poison’s effects to the normal attack damage.",
        "Minor Effect Suggestions": "No one but the foe notices that you make the attack.",
        "Tiers": {
            '1': {
                "Surprise Attack":
                    "If attacking from a hidden vantage, with surprise, or before an opponent has acted, you gain an "
                    "asset to your attack. On a successful hit with this surprise attack, you inflict 2 additional "
                    "points of damage. Enabler.",
                "Natural Assassin": "You are trained in stealth and disguise tasks. Enabler."
            },
            '2': {
                "Quick Death":
                    "(2 Speed points) You know how to kill quickly. When you hit with a melee or ranged attack, you "
                    "deal 4 additional points of damage. You can’t make this attack in two consecutive rounds. Action.",
                "Infiltrator": "You are trained in interactions involving lies or trickery. Enabler."
            },
            '3': {"CHOICE": {
                "Awareness":
                    "(3 Intellect points). You become hyperaware of your surroundings in order to better locate your "
                    "next victim. For ten minutes, you are aware of all living things within long range (including "
                    "their general position), and by concentrating (another action), you can attempt to learn the "
                    "general health and power level of any one of them. Action.",
                "Poison Crafter":
                    "You are trained in crafting, sensing, identifying, and resisting poisons. Your poison crafting "
                    "has given you some immunity to poisons; you have +5 Armor that applies specifically to poison "
                    "damage. Enabler.",
            }},
            '4': {
                "Better Surprise Attack":
                    "If attacking from a hidden vantage, with surprise, or before an opponent has acted, your attack "
                    "is eased by two steps instead of one. On a successful hit with this surprise attack, you inflict "
                    "2 additional points of damage (for a total of 4 additional points of damage). Enabler."
            },
            '5': {
                "Slayer (5 Speed points)":
                    "With a swift and sudden attack, you strike a foe in a vital spot. If the target is level 3 or "
                    "lower, it is killed outright. Action."
            },
            '6': {"CHOICE": {
                "Escape Plan":
                    "When you kill a foe, you can attempt a sneaking action to immediately hide from anyone around, "
                    "assuming that a suitable hiding place is nearby. Enabler.",
                "Murderer":
                    "(8+ Speed points) With a swift and sudden attack, you strike a foe in a vital spot. If the "
                    "target is level 4 or lower, it is killed outright. For each additional level of Effort you apply, you can increase the level of the target by 1. Action."
            }}
        }
    },
    "Rages": {
        "Description": "The berserker is a feared fighter who cannot be stopped. You put yourself into a howling "
                       "battle frenzy that can make you a terror on the battlefield. You might hail from a less "
                       "civilized society, perhaps even a tribal one.",
        "Connection": [
            "Choose one other PC. You feel strangely protective toward that character and don’t want to see them come "
            "to harm.",
            "Pick one other PC. That character knows a secret about your past that is tied to your Frenzy ability.",
            "Pick one other PC. The first time you went into a frenzy was in an attempt to save their loved one from "
            "an attack. You failed, partly because of your inexperience.",
            "Choose one other PC. That character is terrified by your rage and sometimes can’t help but flee at "
            "inopportune times."
        ],
        "Additional Equipment": [],
        "Core Features": {},
        "Major Effect Suggestions": "Your foe is terrified of your rage and uses its next two actions to flee.",
        "Minor Effect Suggestions": "When fighting multiple foes, you knock one into another, putting both off "
                                    "balance and hindering them for one round.",
        "Tiers": {
            '1': {
                "Frenzy":
                    "(1 Intellect point) When you wish, while in combat, you can enter a state of frenzy. While in "
                    "this state, you can’t use Intellect points, but you gain +1 to your Might Edge and your Speed "
                    "Edge. This effect lasts as long as you wish, but it ends if no combat is taking place within "
                    "range of your senses. Enabler."
            },
            '2': {
                "Hardy":
                    "You gain +5 to your Might Pool. These additional points can be used only to absorb damage. "
                    "You can’t spend them to apply Effort to rolls. Enabler.",
                "Mobile Fighter": "You are trained in climbing and jumping tasks. Enabler."
            },
            '3': {
                "Unarmored Fighter": "While unarmored, you are trained in Speed defense tasks. Enabler.",
                "CHOICE": {
                    "Ignore the Pain":
                        "Your rage makes minor wounds seem insignificant. While you are in a state of frenzy, gain +1 "
                        "to your Armor. Enabler.",
                    "Power Strike":
                        "(3+ Might points) If you successfully attack a target, you knock it prone in addition to "
                        "inflicting damage. The target must be your size or smaller. You can knock down a target larger"
                        " than you if you apply a level of Effort to do so (rather than to ease the attack). Enabler."
            }},
            '4': {
                "Greater Frenzy":
                    "(4 Intellect points) When you wish, while in combat, you can enter a state of frenzy. While in "
                    "this state, you can’t use Intellect points, but you gain +2 to your Might Edge and your Speed "
                    "Edge. This effect lasts as long as you wish, but it ends if no combat is taking place within "
                    "range of your senses. You can use this ability or your first-tier Frenzy ability, but you can’t "
                    "use both at the same time. Enabler."
            },
            '5': {
                "Attack and Attack Again":
                    "Rather than granting additional damage or a minor or major effect, a natural 17 or higher on "
                    "your attack roll allows you the option of immediately making another attack. Enabler."
            },
            '6': {"CHOICE":{
                "Not Dead Yet":
                    "When you would normally die, you instead fall unconscious for one round and then awaken. You "
                    "immediately gain 1d6 +6 points to restore your stat Pools and are treated as if debilitated "
                    "(which for you is like being impaired, thanks to your Ignore the Pain ability) until "
                    "you rest for ten hours. If you die again before you make your ten-hour recovery roll, you are "
                    "truly dead. Enabler.",
                "Tough and Fast":
                    "You gain +6 to your Might Pool and your Speed Pool. Enabler."
            }}
        }
    },
    "Rides the Lightning": {
        "Description": "The ancients harnessed electricity in strange and wonderful ways. Through practice and "
                       "inherent ability (or the subtle use of hidden or implanted devices), you control the same "
                       "energy. Not only can you create and discharge electrical power, but you can eventually learn "
                       "to use it to transport yourself.",
        "Connection": [
            "Pick one other PC. This character has been your friend for a long time, and you have learned to bring "
            "them along when you ride the lightning. If the character is standing right next to you, you can take "
            "them with you when you use the Bolt Rider or Electrical Flight powers. (Normally, neither ability allows "
            "you to transport other creatures.)",
            "Pick two other PCs. You know about an important connection between them that even they don’t know about.",
            "Pick one other PC. This character has interesting ideas about electricity and how it can be harnessed. "
            "If you are trained with machines, after you talk to this character for an hour, you gain an asset on any "
            "task involving identifying, crafting, or repairing a machine that uses electricity.",
            "Pick one other PC. This person has the worst luck with electrical devices of anyone you’ve ever met. "
            "You want to help them, but you aren’t sure how or even whether they will be open to your assistance.",
        ],
        "Additional Equipment": ["a bag of miscellaneous batteries and power cells. Whenever you find a new device "
                                 "that operates on batteries or cells (GM’s discretion), there is a 75 percent chance "
                                 "that the bag contains one that will power the device if it depletes."],
        "Core Features": {
            "Electrical Abilities":
                "If you have abilities that would normally use force or other energy, they instead use "
                "electricity. For example, a Flash or an Onslaught force blast is a blast of lightning. "
                "This alteration changes nothing other than the type of damage and the fact that it "
                "might start fires."
        },
        "Major Effect Suggestions": "Devices filled with electrical power explode. You can target and destroy an "
                                    "artifact that a foe is holding or wearing.",
        "Minor Effect Suggestions": "The target is dazed by electricity for one round, hindering all of its tasks. "
                                    "Electricity can also shut down an automaton for one round.",
        "Tiers": {
            '1': {
                "Shock":
                    "(1 Intellect point) Your hands crackle with electricity, and the next time you touch a creature, "
                    "you inflict 3 points of damage. Alternatively, if you wield a weapon, for ten minutes it crackles "
                    "with electricity and inflicts 1 additional point of damage per attack. Action for touch; enabler "
                    "for weapon.",
                "Charge":
                    "(1+ Intellect points) You can charge an artifact or other device (except a cypher) so that it "
                    "can be used once. The cost is 1 Intellect point plus 1 point per level of the device. Action."
            },
            '2': {
                "Bolt Rider":
                    "(4 Intellect points). You can move a long distance from one location to another almost "
                    "instantaneously, carried by a bolt of lightning. You must be able to see the new location, and "
                    "there must be no intervening barriers. Action.",
            },
            '3': {
                "Lightning Swift": "You gain +1 to your Speed Edge. Enabler.",
                "CHOICE": {
                    "Drain Charge":
                        "You can drain the power from an artifact or device, allowing you to regain 1 Intellect "
                        "point per level drained. You regain points at the rate of 1 point per round and must give "
                        "your full concentration to the process each round. The GM determines whether the device is "
                        "fully drained (likely true of most handheld or smaller devices) or retains some power "
                        "(likely true of large machines). Action to initiate; action each round to drain.",
                    "Electric Armor":
                        "(4 Intellect points) When you wish it, electricity crackles across your body for ten minutes, "
                        "granting you +1 to Armor. While electrified, you have an additional +2 to Armor versus "
                        "electrical damage specifically, and you inflict 2 points of damage on any creature that "
                        "touches you or attacks you with a melee weapon that conducts electricity. Enabler."
                }
            },
            '4': {
                "Bolts of Power":
                    "(5+ Intellect points) You blast a fan of lightning out to short range in an arc that is "
                    "approximately 50 feet (15 m) wide at the end. This discharge inflicts 4 points of damage. If "
                    "you apply Effort to increase the damage rather than to ease the task, you deal 2 additional "
                    "points of damage per level of Effort (instead of 3 points); however, targets in the area take "
                    "1 point of damage even if you fail the attack roll. Action.",
            },
            '5': {
                "Electrical Flight":
                    "(5 Intellect points) You exude an aura of crackling electricity that lets you fly a long "
                    "distance each round for ten minutes. You can’t carry other creatures with you. Action to activate."
            },
            '6': {"CHOICE":{
                "Flash Across the Miles":
                    "(6+ Intellect points). You can move to an open location on the earth that you’re familiar with "
                    "almost instantaneously, transformed into a bolt of lightning. If you apply a level of Effort, "
                    "you can attempt to penetrate covered locations that you’re aware of as long as a route exists "
                    "from the open air to the area you want to reach that electricity can easily follow. Action.",
                "Wall of Lightning":
                    "(6 Intellect points) You create a barrier of crackling electricity up to 2,500 square feet "
                    "(230 sq. m) in size, shaped as you wish. The wall is a level 7 barrier. Anyone within immediate "
                    "distance of the wall automatically takes 10 points of damage. The wall lasts for one hour. "
                    "Action to create."
            }}
        }
    },
    "Speaks With a Silver Tongue": {
        "Description": "You are poetry incarnate. The words flow from your tongue like liquid metal. Your voice is "
                       "golden and captivating. With enough time and focus, you can convince almost anyone to do "
                       "almost anything for you, with you, or in spite of you. Words—words are what matter. You "
                       "believe they have power. There’s a chance you don’t care much about your appearance, as long "
                       "as you can say what you want to say.",
        "Connection": [
            "Pick one other PC. That character seems overly affected by your words. You’ve accidentally made them cry "
            "or laugh just by talking to them.",
            "Pick one other PC. That character believes that you speak falsely and is never affected by your words.",
            "Pick one other PC. You’d like to get to know them better, but don’t want to use your skills to do so.",
            "Pick one other PC. That character would like to learn your storytelling techniques, and you’re trying to "
            "decide whether to teach them."
        ],
        "Additional Equipment": ["a book in which you keep notes of your favorite words, inspirational stories, and "
                                 "speech anecdotes."],
        "Core Features": {},
        "Major Effect Suggestions": "You speak with extra conviction, increasing the effect, duration, or range of "
                                    "your action.",
        "Minor Effect Suggestions": "The next time you attempt to influence, persuade, or deceive the same foe, the "
                                    "task is eased.",
        "Tiers": {
            '1': {
                "Poetic License":
                    "You are trained in all social interactions, including persuasion, deception, and intimidation. "
                    "You also know two languages other than the Truth. Enabler."
            },
            '2': {
                "A Smile and a Word":
                    "When you use Effort on any action involving interactions—even those having to do with calming "
                    "animals or communicating with someone or something whose language you do not speak—you gain a "
                    "free level of Effort on the task. Action."
            },
            '3': {"CHOICE": {
                "Verbal Misdirection":
                    "(2+ Intellect points) With fast talk and bewildering words, you can confuse and distract anyone "
                    "that you’re speaking with, giving you an asset on social interactions with that person for ten "
                    "minutes. For each level of Effort you use with this ability, you can affect an additional "
                    "creature. Enabler.",
                "Play to the Crowd":
                    "(3 Intellect points) You give a speech that is both rousing and terrifying. Those within short "
                    "range who can hear and understand you have their next action either eased (an asset) or "
                    "hindered—you choose, and it can be different for each individual.",
            }},
            '4': {
                "Castigate":
                    "(4 Intellect points) You intimidate any opponent within long range who understands speech "
                    "(even if it is not your language) so much that they lose their next action and all the rest "
                    "of their actions are hindered for one minute. Action."
            },
            '5': {
                "Stay the Course":
                    "(5 Intellect points) When your companions are flagging, you can help inspire them with a "
                    "well-timed word or two. Any ally (except you) within immediate range can make a recovery roll "
                    "that is not an action and does not count toward their daily limit. Action."
            },
            '6': {"CHOICE":{
                "Entrancing Speech":
                    "(6 Intellect points) Everyone within long range who can hear and understand you takes no action "
                    "for as long as you do not move and use your action to speak soothing and calming words. If an "
                    "affected creature is attacked during this time, they break out of the trance immediately. "
                    "Action to initiate.",
                "Command":
                    "(7 Intellect points) A target within short range obeys any command you give as long as they can "
                    "hear and understand you. Further, as long as you continue to do nothing but issue commands "
                    "(taking no other action), you can give that same target a new command. This effect ends when you "
                    "stop issuing commands or they are out of short range. Action to initiate.",
            }}
        }
    },
    "Talks to Machines": {
        "Description": "Since you were young, you had an affinity for machines. It seemed almost like you were "
                       "speaking to them.\nYou were. You have the ability to use your organic brain like an "
                       "intelligent machine, interfacing “wirelessly” with any electronic device. You can control "
                       "and influence them in ways that others can’t. Intelligent machines are your friends and "
                       "companions. You have also learned to repair machines of all kinds because the better they "
                       "work, the better off you are as well.",
        "Connection": [
            "Pick one other PC. That character seems to have a terrible relationship with machines—or at least the "
            "machines that you communicate with. If that person is next to a machine that you interact with in a "
            "friendly manner, that machine is treated in all ways as being 1 level lower than normal (unless doing so "
            "benefits you or them, in which case the level does not change).",
            "Pick one other PC. That person seems especially leery of you, though this could just be your perception.",
            "Pick one other PC. That character has a small machine among their equipment but won’t tell you any "
            "details about it or let you see it.",
            "Pick one other PC. You know that this character knows an incriminating or embarrassing secret about you, "
            "and you hope that they do not reveal it."
        ],
        "Additional Equipment": ["A bag of small tools."],
        "Core Features": {},
        "Major Effect Suggestions": "The duration of influence or control becomes 28 hours.",
        "Minor Effect Suggestions": "The duration of influence or control is doubled.",
        "Tiers": {
            '1': {
                "Machine Affinity": "You are trained in tasks involving electrical machines. Enabler.",
                "Distant Activation":
                    "(1 Intellect point) You can activate or deactivate any machine you can see within short range, "
                    "even if normally you would have to touch or manually operate the device. To use this ability, "
                    "you must understand the function of the machine, it must be your size or smaller, and it can’t "
                    "be connected to another intelligence (or be intelligent itself). Action.",
            },
            '2': {
                "Coaxing Power": "(2 Intellect points) You boost the power or function of a machine so that it "
                                 "operates at 1 level higher than normal for one hour. Action to initiate.",
                "Charm Machine":
                    "(2 Intellect points). You convince an unintelligent machine to “like” you. A machine that likes "
                    "you is 50 percent less likely to function if said function would cause you harm. Thus, if a foe "
                    "attempts to detonate a bomb near you controlled by a detonator that likes you, there is a 50 "
                    "percent chance that it won’t explode. Action to initiate.",
            },
            '3': {"CHOICE":{
                "Command Machine":
                    "(4 Intellect points). If you’ve charmed an unintelligent machine or have spoken telepathically "
                    "with an intelligent machine, you can attempt to command it to take one action within its "
                    "capabilities on its next turn. (If you command an intelligent machine with this power, it "
                    "likely becomes hostile to you afterward.) Action.",
                "Intelligent Interface":
                    "(3 Intellect points) You can speak telepathically with any intelligent machine within long "
                    "range. Further, you are trained in all interactions with intelligent machines. Such machines "
                    "and automatons that normally would never communicate with a human might talk to you. Enabler."
            }},
            '4': {
                "Machine Companion":
                    "You create a level 3 animate, intelligent machine that accompanies you and acts as you direct. As "
                    "a level 3 machine companion, it has a target number of 9 and 9 health, and it inflicts 3 points "
                    "of damage. If it’s destroyed, it takes you one month to create a new one. Enabler.",
                "Automaton Fighter":
                    "When fighting an automaton or intelligent machine, you are trained in attacks and defense. "
                    "Enabler."
            },
            '5': {
                "Information Gathering":
                    "(5 Intellect points). You speak telepathically with any or all machines within 1 mile (1.5 km). "
                    "You can ask one basic question about themselves or anything happening near them and receive a "
                    "simple answer. For example, while in an area with many machines, you could ask “Where is the "
                    "ravage bear?” and if the creature is within a mile of you, one or more machines will probably "
                    "provide the answer. Action."
            },
            '6': {"CHOICE":{
                "Improved Machine Companion":
                    "Your machine companion improves, becoming a level 5 creature with the ability either to fly a "
                    "long distance each round (and carry you) for up to ten minutes at a time, or to carry an extra "
                    "cypher for you that doesn’t count against your cypher limit. Enabler.",
                "Control Machine":
                    "(6 Intellect points) You can attempt to control the functions of any machine, intelligent or "
                    "otherwise, within short range for ten minutes. Action."
            }}
        }
    },
    "Wears a Sheen of Ice": {
        "Description": "Through your studies, you have learned to focus your natural talents to command the powers of "
                       "ice and cold. People might refer to you as an ice mage. Sometimes ice mages are thought to "
                       "come into conflict with those known as fire mages, but this is a fallacy believed by ordinary "
                       "folks more than anything based in truth.",
        "Connection": [
            "Pick one other PC. Due to a quirk of the numenera, if that character is standing next to you when you "
            "use your Ice Armor ability, they are also protected by a sheen of ice. (They do not get the added "
            "protection of your Resilient Ice Armor ability.)",
            "Pick one other PC. For a reason unknown to you, their very presence seems to heat the air around you, "
            "making it more difficult to command the powers of ice and cold. If they are within immediate range, "
            "their presence occasionally hinders your attempts to hit a target with a focus ability.",
            "Pick one other PC. That person is especially susceptible to the cold that radiates from you. How they "
            "handle that vulnerability is up to them.",
            "Pick one other PC. The two of you have a long history and almost always disagree about the best way to "
            "handle situations."
        ],
        "Additional Equipment": [],
        "Core Features": {
            "Ice Abilities":
                "If you possess abilities that would normally use force or other energy, they instead use cold and "
                "ice. For example, a force blast is a ray of frost. This alteration changes nothing other than the "
                "type of damage. As another example, Barrier creates a wall of ice. This alteration changes nothing "
                "except the wall’s appearance and the fact that it takes 2 additional points of damage from fire."
        },
        "Major Effect Suggestions": "The target is covered in ice that slows its movement and hinders its tasks for "
                                    "one minute.",
        "Minor Effect Suggestions": "The surface around the target becomes slick and difficult to stand on.",
        "Tiers": {
            '1': {
                "Ice Armor":
                    "(1 Intellect point). When you wish it, your body is covered in a sheen of ice for ten minutes "
                    "that gives you +1 to Armor. While the sheen is active, you feel no discomfort from normal cold "
                    "temperatures and have an additional +2 to Armor versus cold damage specifically. Enabler."
            },
            '2': {
                "Frost Touch":
                    "(1 Intellect point) Your hands become so cold that the next time you touch a creature, you "
                    "inflict 3 points of damage. Alternatively, you can use this ability on a weapon, and for ten "
                    "minutes, it inflicts 1 additional point of damage from the cold. Action for touch; enabler for "
                    "weapon."
            },
            '3': {"CHOICE":{
                "Freezing Touch":
                    "(4 Intellect points) Your hands become so cold that, in addition to inflicting damage as "
                    "described under Frost Touch, your touch freezes solid a living target of your size or smaller, "
                    "rendering it immobile for one round. Action.",
                "Ice Creation":
                    "(4+ Intellect points). You create a solid object of ice that is your size or smaller. The object "
                    "is crude and can have no moving parts, so you can make a sword, a shield, a short ladder, and so "
                    "on. Your ice objects are as strong as iron, but if you’re not in constant contact with them, they "
                    "function for only 1d6 + 6 rounds before breaking or melting. For example, you can make and wield "
                    "an ice sword, but if you give it to another PC, the sword won’t last as long for that character. "
                    "In addition to the normal options for using Effort, you can choose to use Effort to create "
                    "objects larger than you. For each level of Effort used in this way, you can create an object up "
                    "to twice again as large as you. Action."
            }},
            '4': {
                "Resilient Ice Armor":
                    "The sheen of ice you generate using your Ice Armor ability gives you an additional +1 to Armor. "
                    "Enabler."
            },
            '5': {
                "Cold Burst":
                    "(5+ Intellect points). You emit a burst of cold in all directions, up to short range. All "
                    "within the burst take 5 points of damage. If you apply Effort to increase the damage rather than "
                    "to ease the task, you deal 2 additional points of damage per level of Effort (instead of 3 "
                    "points); however, targets in the area take 1 point of damage even if you fail the attack roll. "
                    "Action."
            },
            '6': {"CHOICE": {
                "Ice Storm":
                    "You attempt an additional Intellect task as part of your Cold Burst attack, and if successful, "
                    "you blind foes for up to one minute with a layer of freezing ice. All tasks of blinded creatures "
                    "are hindered by two steps. Enabler.",
                "Winter Gauntlets":
                    "When you use Frost Touch, you inflict a total of 5 points of damage if you touch a creature, or "
                    "+2 points of damage if you infuse a weapon. In addition, damaged targets are frozen in place (if "
                    "standing on a solid surface) and can’t move from their location until they use an action to "
                    "break free. The target can still attack and defend. Action for touch; enabler for weapon."
            }}
        }
    },
    "Wields Power with Precision": {
        "Description": "Not only are you blessed with a great command of the numenera, but you are also trained to "
                       "exploit esoteries in ways that elevate you above other Nanos. Some people believe that those "
                       "who perform esoteries are born with the ability, but you know that skill and intelligence "
                       "play important roles. The ancients created the numenera through knowledge, discovery, and "
                       "intellect, and to use it properly, you must follow the same path.",
        "Connection": [
            "Pick one other PC. You’ve placed an immutable, one-time ward that renders them immune to the esoteries "
            "you perform unless they want to be affected.",
            "Pick one other PC. Due to some quirk of the numenera, you can occasionally (and accidentally) share your "
            "powers with them, which gives them an asset on any task they attempt using their esoteries.",
            "Pick one other PC. That character doesn’t seem to trust or like you, but you feel compelled to win "
            "them over.",
            "Pick one other PC. You’ve noticed that they have a book in their possession that you’d very much like "
            "to study, but you’re unsure how to ask them about it."
        ],
        "Additional Equipment": ["an additional book about the numenera."],
        "Core Features": {},
        "Major Effect Suggestions": "The special ability terrifies the target, who uses its next two turns to flee.",
        "Minor Effect Suggestions": "The special ability overwhelms and dazzles the target for one round, "
                                    "hindering it.",
        "Tiers": {
            '1': {
                "Genius": "Your Intellect Pool increases by 5 points. Enabler."
            },
            '2': {
                "Training and Precision":
                    "You are trained in all esoteries. As a result, you ease any task involved in the use of "
                    "an esotery. Enabler.",
            },
            '3': {"CHOICE":{
                "Enhanced Esoteries":
                    "Your esoteries that have durations last twice as long. Your esoteries that have short ranges "
                    "reach to long range instead. Your esoteries that inflict damage deal 1 additional point of "
                    "damage. Enabler.",
                "Versatile Mind":
                    "When you make a Speed defense roll, you can use your Intellect in place of your Speed. Enabler."
            }},
            '4': {
                "Greater Repertoire":
                    "You can learn one additional esotery of fourth tier or lower. Enabler."
            },
            '5': {
                "Greater Training":
                    "You are specialized in all esoteries. As a result, you ease any task involved in the use of an "
                    "esotery by two steps. Enabler."
            },
            '6': {"CHOICE": {
                "Enhanced Esoteries":
                    "If you chose Enhanced Esoteries as your tier 3 option, your esoteries that have durations last "
                    "three times as long. Your esoteries that have short ranges reach to very long range instead. "
                    "Your esoteries that inflict damage deal 2 additional points of damage. If you didn’t take "
                    "Enhanced Esoteries at tier 3, you gain the advantages noted there now. Enabler.",
                "Supra-Genius":
                    "Your Intellect Pool increases by 5, and your Intellect Edge increases by 1. Enabler."
            }}
        }
    },
    "Wields Two Weapons at Once": {
        "Description": "You bear steel with both hands, ready to take on any foe. You fight with two weapons in "
                       "melee, sometimes called dual wielding. A fearsome warrior, quick and strong, you believe "
                       "that the best defense is a strong offense.",
        "Connection": [
            "Pick one other PC. You have trained with this character so much that if the two of you stand back to "
            "back in a fight, you both gain an asset to Speed defense tasks.",
            "Pick one other PC. This character always seems to inadvertently foil your actions, or at least make "
            "them more difficult. If they are within immediate range, actions related to this focus are hindered.",
            "Pick one other PC. You recently had a weapon go missing, and you’re becoming convinced that they took "
            "it. Whether or not they did is up to them.",
            "Pick one other PC. You used to dislike them immensely, but as you get to know this person, you’re "
            "growing more fond of them against your better judgment."
        ],
        "Additional Equipment": ["an additional light melee weapon."],
        "Core Features": {},
        "Major Effect Suggestions": "You can make an immediate additional attack with one of your weapons.",
        "Minor Effect Suggestions": "The target is intimidated and flees as its next action.",
        "Tiers": {
            '1': {
                "Dual Light Wield":
                    "You can use two light weapons at the same time, making two separate attacks on your turn as a "
                    "single action. You remain limited by the amount of Effort you can apply on one action, but "
                    "because you make separate attacks, your opponent’s Armor applies to both. Anything that modifies "
                    "your attack or damage applies to both attacks, unless it’s specifically tied to one of the "
                    "weapons. Enabler."
            },
            '2': {
                "Double Strike":
                    "(3 Might points). When you wield two weapons, you can choose to make one attack roll against a "
                    "foe. If you hit, you inflict damage with both weapons plus 2 additional points of damage, and "
                    "because you made a single attack, the target’s Armor is subtracted only once. Action."
            },
            '3': {"CHOICE":{
                "Dual Medium Wield":
                    "You can use two light weapons or medium weapons at the same time (or one light weapon and one "
                    "medium weapon), making two separate attacks on your turn as a single action. This ability "
                    "otherwise works like the Dual Light Wield ability. Enabler.",
                "Precise Cut": "You inflict +1 damage with light weapons. Enabler."
            }},
            '4': {
                "Dual Defense":"When you wield two weapons, you are trained in Speed defense tasks. Enabler."
            },
            '5': {
                "Dual Distraction":
                    "(1+ Speed points) When you wield two weapons, your opponent’s next attack is hindered, and if "
                    "you apply Effort to your next attack against that same foe, you get a free level of Effort on "
                    "the task. Enabler."
            },
            '6': {"CHOICE":{
                "Disarming Attack":
                    "(5 Speed points). You attempt a Speed task to disarm a foe as part of your melee attack. If you "
                    "succeed, your attack inflicts 3 additional points of damage and the target’s weapon is knocked "
                    "from their grip, landing up to 20 feet (6 m) away. If you fail, you still attempt your normal "
                    "attack, but you don’t inflict the extra damage or disarm the opponent if you hit. Action.",
                "Whirling Dervish":
                    "When you wield two weapons, you can attack up to six times in one round as a single action, "
                    "but you must make each attack against a different foe. Make a separate attack roll for each "
                    "attack. You remain limited by the amount of Effort you can apply on one action, but because "
                    "you make separate attacks, Armor applies to each of them. Anything that modifies your attack or "
                    "damage applies to all attacks (positively or negatively), unless it’s specifically tied to one "
                    "of the weapons, in which case it applies to only half of the attacks. Enabler."
            }}
        }
    },
    "Works the Back Alleys": {
        "Description": "The thief, the burglar, the pickpocket: these are the dangerous individuals who haunt the "
                       "back alleys of every community. You are a thief in a city or town, making your livelihood at "
                       "the expense of the wealthy. Your talents, however, prepare you for all kinds of pursuits, "
                       "even when you’re not crouching in an alley or climbing into a window.",
        "Connection": [
            "Pick one other PC. The character knew you beforehand and convinced you to leave your life of crime for "
            "other pursuits—at least temporarily.",
            "Pick one other PC. A while back, you attempted to “borrow” something from this person, but they caught "
            "you in the process. You managed to convince them that it was a simple misunderstanding, but they may not "
            "entirely trust you.",
            "Pick one other PC. You never seem to be able to hide so that this person can’t see you.",
            "Pick one other PC. This character knows your real identity (if it’s a secret) or that you work secretly "
            "as a thief (if it’s a secret) and has kept the knowledge safe so far. It’s up to them whether they "
            "continue to do so."
        ],
        "Additional Equipment": ["a bag of light tools."],
        "Core Features": {},
        "Major Effect Suggestions": "You can immediately take a second action during this turn.",
        "Minor Effect Suggestions": "You can immediately attempt to hide after this action.",
        "Tiers": {
            '1': {
                "Thief": "You are trained in sneaking, pickpocketing, and lockpicking tasks. Enabler."
            },
            '2': {
                "Underworld Contacts":
                    "You know many people in a variety of communities who engage in illegal activities. These people "
                    "are not necessarily your friends and might not be trustworthy, but they recognize you as a peer. "
                    "You and the GM should work out the details of your underworld contacts. Enabler."
            },
            '3': {"CHOICE":{
                "Pull a Fast One":
                    "(3 Intellect points) When you’re running a con, picking a pocket, fooling or tricking a dupe, "
                    "sneaking something by a guard, and so on, you gain an asset on the task. Enabler.",
                "Guild Training":
                    "Your type abilities that have durations last twice as long. Your type abilities that have short "
                    "ranges reach to long range instead. Your type abilities that inflict damage deal 1 additional "
                    "point of damage. Enabler."
            }},
            '4': {
                "Master Thief":
                    "You are trained in climbing, escaping from bonds, slipping through narrow places, and other "
                    "contortionist moves. Enabler."
            },
            '5': {
                "Dirty Fighter":
                    "(2 Speed points). You distract, blind, annoy, hamper, or otherwise interfere with a foe, "
                    "hindering their attacks and defenses for one minute. Action."
            },
            '6': {"CHOICE":{
                "Alley Rat":
                    "(6 Intellect points). While in a city, you find or create a significant shortcut, secret "
                    "entrance, or emergency escape route where it looked like none existed. Doing so requires that "
                    "you succeed on an Intellect action whose difficulty is set by the GM based on the situation. "
                    "You and the GM should work out the details. Action.",
                "All-Out Con":
                    "(7 Intellect points). You put everything into it. You add three free levels of Effort to the "
                    "next task you attempt. You can’t use this ability again until after you’ve taken a ten-hour "
                    "recovery action. Action."
            }}
        }
    },
    "Works Miracles": {
        "Description": "You manipulate matter and time to help others and are beloved by everyone you encounter. Some "
                       "people consider you a representative of the gods or a power from beyond this world. Perhaps "
                       "they’re right—transdimensional experiments in the prior worlds might be what created the "
                       "energies that you now wield.",
        "Connection": [
            "Pick one other PC. This character quietly suspects that you’re a messiah or supernatural being.",
            "Pick one other PC. This person knows a secret of yours, and you desperately hope that they do not tell "
            "anyone. You can choose whether or not you’re aware of their suspicion.",
            "Pick one other PC. This character believes that you cured someone close to them of a deadly disease, and "
            "they are grateful. You aren’t sure whether you actually helped or if that person wasn’t as sick as was "
            "thought.",
            "Pick one other PC. You secretly believe that this person might be a hypochondriac, and you’re never "
            "sure whether they actually need your help."
        ],
        "Additional Equipment": [],
        "Core Features": {},
        "Major Effect Suggestions": "The target is healed for 2 additional points.",
        "Minor Effect Suggestions": "The target is healed for 1 additional point.",
        "Tiers": {
            '1': {
                "Healing Touch":
                    "(1 Intellect point) With a touch, you restore 1d6 points to one stat Pool of any creature. "
                    "This ability is a difficulty 2 Intellect task. Each time you attempt to heal the same creature, "
                    "the task difficulty increases by one step. The difficulty returns to 2 after that creature rests "
                    "for ten hours. Action."
            },
            '2': {
                "Alleviate": "(3 Intellect points) You attempt to cancel or cure one malady (such as disease or "
                             "poison) in one creature. Action."
            },
            '3': {"CHOICE":{
                "Font of Healing. With your approval, other creatures can touch you and regain 1d6 points to either "
                "their Might Pool or their Speed Pool. This healing costs them 2 Intellect points. A single creature "
                "can benefit from this ability only once each day. Enabler.",
                "Miraculous Health. When you would descend a step on the damage track, you can attempt a Might task "
                "to resist, with a difficulty equal to the level of the foe or effect that harmed you. If successful, "
                "you don’t descend the step and you regain 1 point in any Pool that is bereft of points. You can’t "
                "use this ability again until after your next ten-hour rest. Enabler.",
            }},
            '4': {
                "Inspiration":
                    "(4 Intellect points). Through mental inspiration and the manipulation of time, one creature "
                    "you choose within short range is granted an additional, immediate action, which it can take "
                    "out of turn. Action."
            },
            '5': {
                "Undo":
                    "(5 Intellect points). You turn back time a few seconds, effectively undoing a single creature’s "
                    "most recent action. That creature can then immediately repeat the same action or try something "
                    "different. Action."
            },
            '6': {"CHOICE":{
                "Greater Healing Touch":
                    "(4 Intellect points) You touch a creature and restore its Might Pool, Speed Pool, and Intellect "
                    "Pool to their maximum values, as if it were fully rested. A single creature can benefit from this "
                    "ability only once each day. Action.",
                "Restore Life":
                    "(9+ Intellect points) You can attempt to restore life to a dead creature of up to level 3, as "
                    "long as the corpse is no more than a day old and is mostly intact. You can also attempt to "
                    "restore life to a corpse that is much older but is especially well preserved. The difficulty "
                    "of the Intellect task is equal to the level of the creature you’re attempting to restore to "
                    "life. For each additional level of Effort applied, you can attempt to restore the life of a "
                    "creature whose level is 1 higher. When first restored to life, a creature is dazed for at least "
                    "a day, and all tasks they attempt are hindered. Action; one minute to initiate."
            }}
        }
    },  # End Discovery Foci, Start Destiny Foci
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