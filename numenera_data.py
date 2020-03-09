assignable_stat_points = 6

type_template = {
    "Base Stats": [8, 8, 8],
    "Starting Edge": [0, 0, 0],
    "Weapon Proficiencies": [],
    "Class Skills": [],
    "Class Intrusions": {},
    "Cypher Limit": 2,
    "Starting Equipment": {
        "Equipment": [],
        "Shins": 0,
        "Cyphers": [],
        "Oddities": [],
        "Iotum": {},
        "Parts": 0,
        "Artifacts": []
    },
    "Default Cyphers": [],
    "Default Oddity": [],
    "Community Bonus": "",  # remove, add to tier 1
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

discovery_types = {
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
        "Starting Equipment": {
            "Equipment": ["Clothing", "Weapon 1", "Weapon 2 or Shield", "Light or Medium Armor",
                          "If a ranged weapon, 12 Ammo of its type"],
            "Shins": 5,
            "Cyphers": ["Destiny Nodule", "Rejuvinator"],
            "Oddities": ["Shifting Blob of Clay"],
            "Iotum": {},
            "Parts": 0,
        },
        "Community Bonus": "While you are present within a community, and actively and personally working on behalf "
                           "of that community, the community’s effective rank for damage inflicted is +1. Enabler.",
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
                  "Improved Community Defender":
                      "A community continues to modify its effective rank for damage inflicted by +1. However, "
                      "you do not need to be constantly present in and actively working on behalf of the community "
                      "for it to gain this benefit; it gains it merely because of your past defense of the community. "
                      "Enabler.",
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
                  "CHOICE": {
                      "Rampaging Beast Horde":
                          "(12 Might points) You can take community actions with a horde or a community as if you "
                          "were a rank 3 rampaging beast horde for one hour. You can spend a few rounds or minutes "
                          "here and there taking character actions if something requires attention and still retain "
                          "your horde status. For each allied PC that joins you and remains with you during this "
                          "period who also spends 12 points from one of their Pools, you can extend the duration by "
                          "one hour. Each point of damage you take while being treated as a rampaging beast horde is "
                          "deducted from your Might Pool, or if you have allied PCs helping, the damage is split up "
                          "and deducted from all your Might Pools evenly. Action to initiate.",
                      "Recruit Deputy":
                          "You gain a level 4 follower. They are not restricted on their modifications. Enabler.",
                  },
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
        "Starting Equipment": {
            "Equipment": ["Clothing", "Weapon", "Book About The Numenera", ],
            "Shins": 4,
            "Cyphers": ["Gravity Nullifying Spray", "Telepathy Implant", "Teleporter"],
            "Oddity": ["Infinity Thermos", ],
            "Iotum": {},
            "Parts": 0,
        },
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
            '1': {
                "Community Scholar":
                    "While you are present within a community, and actively and personally working on behalf of that "
                    "community, the community’s health and infrastructure are both increased by +1. Enabler.",
                "CHOOSE2": {
                    "Hedge Magic":
                        "(1 Intellect point) You can perform small tricks: temporarily change the color or basic "
                        "appearance of a small object, "
                        "cause small objects to float through the air, clean a small area, mend a broken object, "
                        "prepare (but not create) food, and so on. You can’t use Hedge Magic to harm another creature "
                        "or object. Action.",
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
                  "Improved Community Scholar":
                      "A community continues to modify its health and infrastructure by +1 rank. However, you do not "
                      "need to be constantly present in and actively working on behalf of the community for it to "
                      "gain this benefit; it gains it merely because of your past efforts on the community’s behalf. "
                      "Enabler.",
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
            '4': {"CHOOSE1": {
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
            '6': {
                "Recruit Deputy":
                    "You gain a level 4 follower. They are not restricted on their modifications. Enabler.",
                "CHOOSE1": {
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
        "Starting Edge": "CHOICE",  # Choice: Add one edge to chosen pool
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
        "Starting Equipment": {
            "Equipment": ["Clothing", "Weapon A", "Weapon B", "Light Armor", "An Explorer's Pack",
                          "A Pack of Light Tools"],
            "Cyphers": ["Machine Control Implant", "Visage Changer"],
            "Shins": 8,
            "Oddities": ["Small Square Stasis Cage"],
        },
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
                  "Community Fixer":
                      "While you are present within a community, and actively and personally working on behalf of "
                      "that community, the community’s effective rank for health or infrastructure is increased by "
                      "+1. You choose which is modified during any given community action. Enabler.",
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
                  "Improved Community Fixer":
                      "A community continues to modify its health or infrastructure by +1 rank. However, you do not "
                      "need to be constantly present in and actively working on behalf of the community for it to "
                      "gain this benefit; it gains it merely because of your past efforts on the community’s behalf. "
                      "Whichever stat you modified last remains active until you return and modify it to something "
                      "else. Enabler.",
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
                  "CHOOSE1": {
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
                  "Recruit Deputy":
                      "You gain a level 4 follower. They are not restricted on their modifications. Enabler.",
                  "CHOOSE1": {
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
}

destiny_types = {
    "Arkus": {
        "Base Stats": [8, 9, 11],
        "Starting Edge": [0, 0, 1],
        "Weapon Proficiencies": ["Light"],
        "Class Skills": ["Persuasion", "CHOICE:Interaction Skill"],
        "Class Inabilities": ["Understanding Numenera", "Salvaging Numenera", "Crafting Numenera"],
        "Cypher Limit": 2,
        "Class Intrusions": {
            "Friendly NPC":
                "An NPC you don’t know, someone you don’t know that well, or someone you know but who hasn’t been "
                "particularly friendly in the past chooses to help you, though doesn’t necessarily explain why. "
                "Maybe they’ll ask you for a favor in return afterward, depending on how much trouble they go to.",
            "Perfect Suggestion":
                "A follower or other already-friendly NPC suggests a course of action with regard to an urgent "
                "question, problem, or obstacle you’re facing.",
            "Unexpected Gift":
                "An NPC hands you a physical gift you were not expecting, one that helps put the situation at ease "
                "if things seem strained, or provides you with a new insight for understanding the context of the "
                "situation if there’s something you’re failing to understand or grasp."
        },
        "Starting Equipment": {
            "Equipment": ["stylish clothing", "a light weapon of your choice",
                          "If you start with a ranged weapon that requires ammunition you start with 12"],
            "Shins": 9,
            "Cyphers": ["farspeaker", "harmony lamp"],
            "Oddities": ["feathered hat that occasionally makes bird noises"],
            "Iotum": {},
            "Parts": 0,
        },
        "Community Bonus": "",
        "Connections": [
            "You were in the military and had command over several others who still serve.",
            "You were the head of a wealthy merchant family that lost everything in a disaster.",
            "You owned a tavern for a while, but you sold it to a friend so you could seek greater challenges.",
            "You learned at the feet of an incredibly talented leader who went into hiding for fear of assassination.",
            "Your first love is involved in the ruling council of the community where you spent much of your youth.",
            "One of your grandparents was a minor official, but they were ousted and run out of town on suspicion of "
            "corruption.",
            "You spent some time leading a group of violent rebels but thought better of your actions later.",
            "You once promised to help a negotiation with a group of abhumans that turned out badly.",
            "A flock of traveling murdens always seek you out when they’re nearby because you once helped them.",
            "You are a member of a small secret society.",
            "Your ex-best friend tried to have you arrested on trumped-up charges, so you left town.",
            "You have traveled extensively, and during that time, you accumulated quite a collection of strange "
            "souvenirs.",
            "You grew up in a large, thriving city and still have many friends and contacts back there.",
            "You spoke up for a person you thought was wrongly accused of a crime. They were released partly based on "
            "your testimony, but you later came to have doubts.",
            "As an orphan, you had a difficult childhood, and your entry into adulthood was challenging.",
            "You headed a small church, and though you left to pursue your own strange journey, the congregation still "
            "tries to lure you back to the pulpit.",
            "Before they died, your parent was a respected member of the Order of Truth. Those who knew your parent "
            "are fond of you, but they also expect great things from you.",
            "As a political refugee, you are often treated with suspicion.",
            "When you were a diplomat working for a large city, you made friends with several visiting envoys, some of "
            "whom you still contact.",
            "You were married but lost your spouse in a horrific accident. The protection you failed to offer them is "
            "something you’d like to provide to save others.",
        ],
        "Tiers": {
            '1': {
                "Demeanor of Command":
                    "(2 Intellect points) You emote confidence, knowledge, and charisma to all who see you for "
                    "the next hour. Your demeanor is such that those who see you automatically understand that you "
                    "are someone important, accomplished, and with authority. When you speak, strangers that are not "
                    "already attacking give you at least a round to have your say. If speaking to a group that can "
                    "understand you, you can attempt to have them produce their leader or ask that they take you to "
                    "their leader. You gain a free level of Effort that can be applied to one persuasion task you "
                    "attempt during this period. Action to initiate.",
                "Community Leader":
                    "While you are present within a community, and actively and personally working on behalf of that "
                    "community, the community’s rank is +1 for all purposes except damage inflicted. Enabler.",
                "CHOOSE2": {
                    "Anecdote":
                        "(2 Intellect points) You can lift the spirits of a group of creatures and help them bond "
                        "together by entertaining them with an uplifting or pointed anecdote. For the next hour, "
                        "those who pay attention to your story are trained in a task you choose that’s related to "
                        "the anecdote, as long as it’s not an attack or defense task. Action to initiate, one "
                        "minute to complete.",
                    "Babel":
                        "(3 Intellect points) Once each day, choose one language that you’ve encountered on which "
                        "you will concentrate. For the rest of that day, you can speak that language with reasonable "
                        "facility. You don’t lose the use of any other languages you know normally during this period. "
                        "Action to initiate, ten minutes to complete.",
                    "Connection With an Organization":
                        "You have a general connection with an important organization, such as the Order of Truth, "
                        "the Angulan Knights, the aristocracy of a region, a merchant guild, and so on. Tasks related "
                        "to interacting with members of that group gain an asset. Further, you can use this connection "
                        "to learn about events related to that organization’s focus. For instance, if you have a "
                        "connection with the Angulan Knights, you may learn of events related to mutants in the "
                        "area. You and the GM should work out the details together. You can choose this ability more "
                        "than once and choose a new organization each time. Enabler.",
                    "Goad":
                        "(1 Intellect point) You can attempt to goad a target into a belligerent—and probably "
                        "foolish—reaction that requires the target to try to close the distance between you and "
                        "attempt to physically strike you on its next turn. They attempt this action even if this "
                        "would cause them to break formation or to give up cover or a tactically superior position. "
                        "Whether the target strikes you or fails to do so, they come to their senses immediately "
                        "afterward, after which further tasks attempting to goad the target again are hindered. "
                        "Action to initiate.",
                    "Powerful Rhetoric":
                        "(1 Intellect point) After engaging a creature in conversation for at least a minute, you can "
                        "attempt to influence how that creature is perceived, promoting it as a friend, dismissing it "
                        "as a fool, or denouncing it as an enemy. Your words are so well chosen that even you and it "
                        "are affected, because your conviction and its doubt are paramount. The accuracy of your "
                        "assessment isn’t important as long as you keep up the rhetoric. From then on (or until you "
                        "change your rhetoric or the creature offers a convincing defense to those who’ve heard your "
                        "label), the friend’s social interactions gain an asset, the fool’s social interactions are "
                        "hindered, or the enemy’s defenses are hindered. Action to initiate, one minute to complete.",
                    "Trained Without Armor":
                        "You are trained in Speed defense actions when not wearing armor. Enabler.",
                    "Understanding":
                        "(1 Intellect point) You observe or study a creature or object. Your next interaction with "
                        "that creature or object gains one asset. Action.",
                }
            },
            '2': {"CHOOSE1": {
                "Calm Stranger":
                    "(2+ Intellect points) You can cause one intelligent creature to remain calm as you speak. The "
                    "creature doesn’t need to speak your language, but it must be able to see you. It remains calm as "
                    "long as you focus all your attention on it and it is not attacked or otherwise threatened. In "
                    "addition to the normal options for using Effort, you can also choose to use Effort to calm "
                    "additional creatures allied with your initial target, one additional creature per level of "
                    "Effort applied. Action.",
                "Cloud Personal Memories":
                    "(3 Intellect points) If you interact with or study a target for at least a round, you gain a "
                    "sense of how its mind works, which you can use against it in the most blunt fashion possible. "
                    "You can attempt to confuse it and make it forget what’s just happened. On a success, you erase "
                    "up to the last five minutes of its memory. Action to prepare; action to initiate.",
                "Disincentivize":
                    "(1 Intellect point) You hinder all actions attempted by any number of targets within short range "
                    "who can understand you. You choose which targets are affected. Affected targets’ actions are "
                    "hindered for one round. Enabler.",
                "Follower":
                    "You gain a level 2 follower. One of their modifications must be persuasion. You can take this "
                    "ability multiple times, each time gaining another level 2 follower. Enabler.",
                "Gather Intelligence":
                    "(2 Intellect points) When in a group of people (a caravan, a palace, a village, a city, etc.) "
                    "you can ask around about any topic you choose and come away with useful information. You can ask "
                    "a specific question, or you can simply obtain general facts. You also get a good idea of the "
                    "general layout of the location involved, note the presence of all major sites, and perhaps even "
                    "notice obscure details. For example, not only do you find out if anyone in the palace has seen "
                    "the missing boy, but you also get a working knowledge of the layout of the palace itself, note "
                    "all the entrances and which are used more often than others, and take notice that everyone seems "
                    "to avoid the well in the eastern courtyard for some reason. This ability takes about an hour to "
                    "use.",
                "Inspire Action":
                    "(4 Intellect points) If one ally can see and easily understand you, you can instruct that ally "
                    "to take an action. If the ally chooses to take that exact action, they can do so as an additional "
                    "action immediately. Doing so doesn’t interfere with the ally taking a normal action on their "
                    "turn. Action.",
                "Skill With Defense":
                    "Choose one type of defense task in which you are not already trained: Might, Speed, or Intellect. "
                    "You are trained in defense tasks of that type. You can select this precept up to three times. "
                    "Each time you select it, you must choose a different type of defense task. Enabler.",
            }},
            '3': {
                "Expert Cypher Use": "You can bear three cyphers at a time.",
                "Improved Community Leader":
                    "A community continues to modify its effective rank by +1 for any task except for attack and "
                    "defense. However, you do not need to be constantly present in and actively working on behalf of "
                    "the community for it to gain this benefit; it gains it merely because of your past work in the "
                    "community. Enabler.",
                "CHOOSE1": {
                    "Break the Line":
                        "(4 Intellect points) You have an eye for group discipline and hierarchy, even among your "
                        "foes. If a group of foes is gaining any kind of benefit from working together, you can "
                        "attempt to disrupt that benefit by pointing out the weak point in the enemy’s line, "
                        "formation, or swarm attack. This effect lasts for up to a minute or until all the affected "
                        "foes spend a round assessing and resetting themselves to regain their normal advantage. "
                        "Action to initiate.",
                    "Improved Follower":
                        "You gain a level 3 follower. They are not restricted on their modifications. Alternatively, "
                        "you can choose to advance a level 2 follower you already have to level 3 and then gain a new "
                        "level 2 follower. Enabler.",
                    "Informer":
                        "You gain an informer within an allied community. They act as your secret (or known) informer. "
                        "If something of note happens in your informer’s location, they will use whatever means they "
                        "have available to tell you what’s happened. Enabler.",
                    "Lead by Inquiry":
                        "You keep your allies on their toes with occasional questions, jokes, and even mock drills "
                        "for those who care to join in. After spending 28 hours with you, your allies are treated as "
                        "if trained in tasks related to perception. This benefit is ongoing while you remain in your "
                        "allies’ company. It ends if you leave, but it resumes if you return to the allies’ company "
                        "within 28 hours. If you leave the allies’ company for more than 28 hours, you must spend "
                        "another 28 hours together to reactivate the benefit. Enabler.",
                    "Oratory":
                        "(4 Intellect points) When speaking with a group of intelligent creatures that can understand "
                        "you and aren’t hostile, you convince them to take one reasonable action in the next round. A "
                        "reasonable action should not put the creature or its allies in obvious danger or be wildly "
                        "out of character. Action.",
                    "Perfect Stranger":
                        "(3 Intellect points) You alter your posture and way of speaking and make a small but real "
                        "alteration to an outfit (such as putting on or taking off a hat, reversing a cloak, and so "
                        "on). For the next hour (or as long as you keep up the alteration), even creatures that know "
                        "you well don’t recognize you. All tasks related to hiding your true identity during this "
                        "period gain one free level of Effort. Action to initiate.",
                    "Quick Wits": "When performing a task that would normally require spending points from your "
                                  "Intellect Pool, you can spend points from your Speed Pool instead. Enabler.",
                }
            },
            '4': {"CHOOSE1": {
                "Crowd Protection":
                    "(5 Intellect points) While in an allied community or horde, members who are near you press close "
                    "in a protective formation to keep you safe for about a minute. This crowd moves with you during "
                    "this period, keeping an eye out for anything that might hurt you. When it ends, the crowd "
                    "disperses and individuals go on about their business. The protective crowd makes it harder for "
                    "other creatures to attack you, giving you an asset on Speed defense tasks. In addition, while the "
                    "crowd is around you, you can use an action to exhort them to attack all enemies within short "
                    "range, dealing 1 point of damage to each creature and object in the area. Action to initiate.",
                "Envoy":
                    "(4 Intellect points) If you interact with or study a target that lives within a community "
                    "you’re allied with for at least a round, you can attempt to convince it to become your envoy "
                    "for a specific period or to deliver a specific message or object to another location. Distance "
                    "does not matter as long as the location is somewhere your envoy can reach, either through their "
                    "own means or means you provide. The envoy delivers your message or physical parcel to the "
                    "desired location, and then reports back on whether they succeeded or failed. Action to initiate; "
                    "hours, days, weeks, or months to get a report back.",
                "Exile From Community":
                    "(4 Intellect points) If you are in a community you are allied with and you study a target for "
                    "at least a round, you can attempt to convince them to leave the community, either permanently or "
                    "for a specified period of time. The task is eased if a majority in the community believes that "
                    "the target is a bad seed, troublemaker, criminal, or otherwise someone that makes things "
                    "difficult for the community. Action to prepare; action to initiate.",
                "Spur Effort":
                    "(5 Intellect points) You select an ally within immediate range. If that character applies "
                    "Effort to a task on their next turn, they can apply a free level of Effort on that task. Enabler.",
                "Strategize":
                    "(6 Intellect points) Having an action plan in place before facing a challenge improves the odds "
                    "of success, even if that plan is eventually changed or discarded once it’s put into play. If you "
                    "and your allies spend at least ten minutes going over a plan of action, all of you gain one free "
                    "level of Effort that can be applied to one task you attempt during the execution of that plan "
                    "within the next 28 hours. The plan of action must be something concrete and executable in order "
                    "to gain this benefit. Action to initiate, ten minutes to complete.",
                "Unseen Among the People":
                    "(4+ Intellect points) You become effectively unseen for ten hours while you are within an allied "
                    "community. During this time, the residents help you move from place to place in a variety of ways "
                    "that makes it appear that are no one of importance. While moving unseen in a community, you are "
                    "specialized in stealth and Speed defense tasks. This effect ends if you do something to reveal "
                    "who you really are—attacking, using an ability, commanding someone in the community within "
                    "earshot of an enemy, and so on. If this occurs, you can regain the remaining unseen effect by "
                    "taking an action to focus on going into hiding. You can attempt to move about unseen within an "
                    "unallied community or horde; however, doing so requires that you apply one additional level of "
                    "Effort per rank of the community or horde you wish to hide within. Action to prepare; action to "
                    "initiate or reinitiate.",
            }},
            '5': {
                "Adept Cypher Use": "You can bear four cyphers at a time.",
                "CHOOSE1": {
                    "Discipline of Watchfulness":
                        "(7 Intellect points) You keep your allies on their toes with occasional questions, jokes, "
                        "and even mock drills for those who care to join in. After spending 28 hours with you, your "
                        "allies can apply a free level of Effort to any initiative tasks they attempt. This benefit "
                        "is ongoing while you remain in the allies’ company. It ends if you leave, but it resumes if "
                        "you return to the allies’ company within 28 hours. If you leave the allies’ company for more "
                        "than 28 hours, you must spend another 28 hours together to reactivate the benefit. You must "
                        "spend the Intellect point cost each 28 hours you wish to keep the benefit active. Enabler.",
                    "Divide and Conquer":
                        "(7 Intellect points) If you brief and prep one of your followers or deputies for at least "
                        "a round, they can act on your behalf within an allied community or horde so well that you "
                        "can effectively take on two tasks simultaneously, whether they’re regular actions or "
                        "community tasks. If taking regular actions, you can take two actions on each of your turns "
                        "for up to one minute, including using special abilities of up to tier 3, even in two "
                        "different parts of the community or horde. Special abilities used by your follower or "
                        "deputy are subtracted from your Pools because they are acting on your direct authority and "
                        "are relying on your influence. Alternatively, you can take normal actions while your "
                        "prepped follower attempts a community task, or you can both attempt community tasks. Action "
                        "to prepare; action to initiate.",
                    "Healing Power of Words":
                        "(6 Intellect points) If you interact with or study a target for at least a round, you can "
                        "attempt to restore points to the target’s Might Pool or Speed Pool in one of two ways: "
                        "either the chosen Pool regains up to 6 points or it is restored to a total value of 12 (you "
                        "choose when you initiate this ability). The attempt is a level 3 task. Points are restored "
                        "at a rate of 1 point each round. You must continue speaking with the target the whole time. "
                        "In no case can this ability raise a Pool higher than its normal maximum. Action to prepare; "
                        "action to initiate. If the target spends points from their Pool during the ongoing healing, "
                        "the healing ends.",
                    "Infer Thoughts":
                        "(4 Intellect points) If you interact with or study a target for at least a round, you can "
                        "attempt to read its surface thoughts, even if the subject doesn’t want you to. You must be "
                        "able to see the target. Once you have gained a sense of what it’s thinking—through its body "
                        "language, its speech, and what it does and doesn’t say—you can continue to infer the target’s "
                        "surface thoughts for up to one minute as long as you can still see and hear the target. "
                        "Action to prepare; action to initiate.",
                    "Knowing the Unknown":
                        "(6 Intellect points) While in an allied community or horde, you can spend an action tapping "
                        "into a source of information beyond yourself. You can ask the GM one question and get a "
                        "general answer. The GM assigns a level to the question, so the more obscure the answer, the "
                        "more difficult the task. Generally, knowledge that you could find by looking somewhere other "
                        "than your current location is level 1, and obscure knowledge of the past is level 7. Gaining "
                        "knowledge of the future is impossible. Action to prepare; action to initiate.",
                    "Raise a Champion":
                        "(7 Intellect points) While in an allied community or horde, you can spend a minute rousing "
                        "the community to put forth a champion—a level 5 NPC or creature that could conceivably live "
                        "in and be part of the community. The champion appears for one minute then returns home. "
                        "While present, the champion acts as you direct, requiring no additional actions on your part. "
                        "One minute to prepare; action to initiate.",
                    "Rouse to Violence":
                        "(6+ Intellect points) While in an allied community or horde, you can spend an action rousing "
                        "the ire of residents to a killing frenzy and then point out a target that the crowd can see. "
                        "If you succeed and the target is a creature of level 3 or lower, the crowd kills it. If the "
                        "target is a PC, they move down one step on the damage track. In addition to the normal "
                        "options for using Effort, you can choose to use Effort to increase the maximum level of "
                        "the target (each level of Effort used this way increases the target’s maximum level by 1). "
                        "Action to prepare, action to initiate.",
                    "Suggestion":
                        "(5+ Intellect points) You suggest an action to a creature within immediate range. If the "
                        "action is something that the target might normally do anyway, it follows your suggestion. "
                        "If the suggestion is something that is outside of the target’s nature or express duty (such "
                        "as asking a guard to let an intruder pass), the suggestion fails. The creature must be level "
                        "2 or lower. The effect of your suggestion lasts for up to a minute. In addition to the "
                        "normal options for using Effort, you can also choose to use Effort to increase the maximum "
                        "level of the target you can affect by 1. If its level is higher than 2, you can immediately "
                        "apply levels of Effort to increase the maximum level allowed up to that creature’s level. "
                        "When the effects of the ability end, the creature remembers following the suggestion but can "
                        "be persuaded to believe that it chose to do so willingly. Action to initiate.",
                }
            },
            '6': {
                "Recruit Deputy":
                    "You gain a level 4 follower. They are not restricted on their modifications. Enabler. "
                    "Alternatively, you can choose to advance a level 3 follower you already have to level 4 and "
                    "then gain a new level 3 follower. Enabler.",
                "CHOOSE1": {
                    "Assume Control":
                        "(6+ Intellect points) You control the actions of another creature you have interacted with "
                        "or studied for at least a round. This effect lasts for ten minutes. The target must be level "
                        "2 or lower. Once you have assumed control, the target acts as if it wants to accomplish your "
                        "desire to the best of its ability, freely using its own best judgment unless you use an "
                        "action to give it a specific instruction on an issue-by-issue basis. In addition to the "
                        "normal options for using Effort, you can also choose to use Effort to increase the maximum "
                        "level of the target. Thus, to attempt to command a level 5 target (three levels above the "
                        "normal limit), you must apply three levels of Effort. When the effect ends, the target "
                        "remembers everything that happened and reacts according to its nature and your relationship "
                        "to it; assuming control might have soured that relationship if it was previously a positive "
                        "one. Action to initiate.",
                    "Coax the Crowd":
                        "(7 Intellect points) You convince a large number of people—all within long range—to change "
                        "a belief and take a long-term action or set of actions. For example, you might convince them "
                        "to identify the location of a local criminal that no one has previously been brave enough to "
                        "act against, or you might convince them to welcome a group of visitants as friends in the "
                        "community. This takes ten minutes to accomplish, during which time you can’t be seriously "
                        "interrupted or the attempt automatically fails.",
                    "Extra Community Action":
                        "(9 Intellect points) During the course of a conflict between communities, you can fire up "
                        "one community so much that it can take two community actions in the same amount of time it "
                        "could normally take only one. This means the community could inflict damage twice, inflict "
                        "damage while another segment of the community tries to persuade some other neutral community "
                        "or horde to become allied, or something else. This is considered a community task. Action to "
                        "initiate, one hour to complete.",
                    "Inspiration":
                        "(6 Intellect points) You speak words of encouragement and inspiration. All allies within "
                        "short range who can hear you immediately gain a recovery roll, gain an immediate free "
                        "action, and have an asset for that free action. The recovery roll does not count as one of "
                        "their normal recovery rolls. Action.",
                    "Sway Horde":
                        "(12+ Intellect points) You can attempt to sway a horde of up to rank 2 to disperse or attack "
                        "a community other than the one it is currently targeting, or you can try to raise a horde "
                        "from a village or larger community that contains enough able- bodied adults. If you succeed "
                        "at raising a horde, its level is equal to the rank of the community it comes from, and the "
                        "horde remains cohesive for up to three days or until it is destroyed. In addition to the "
                        "normal options for using Effort, you can also choose to use Effort to increase the rank of "
                        "the horde you sway by 1 for each level of Effort applied. Action to initiate, one hour to "
                        "complete.",
                    "Take Command":
                        "(3 Intellect points) You issue a specific command to another character. If that character "
                        "chooses to listen, any attack they attempt on their next turn is eased, and a hit deals 3 "
                        "additional points of damage. If your command is to perform a task other than an attack, the "
                        "task is eased as if it benefited from a free level of Effort. Action.",
                    "Will of a Leader":
                        "(9 Intellect points) You harden your allies’ dedication and capabilities. Each ally within "
                        "immediate range gains +1 Edge to one stat of their choice for one hour. You also gain this "
                        "benefit to one stat of your choice. Action."
                }
            }
        }
    },
    "Wright": {
        "Base Stats": [9, 7, 12],
        "Starting Edge": [0, 0, 1],
        "Weapon Proficiencies": ["Light"],
        "Class Skills": ["Crafting Numenera", "CHOICE:Crafting Skill", "CHOICE: Another Crafting Skill or Salvaging/"
                                                                       "Understanding Numenera"],
        "Cypher Limit": 3,
        "Class Intrusions": {
            "Device Perfection":
                "A device or installation works even better than you expected it would, at least in this instance. "
                "Maybe the range is twice as long, the duration is 100% longer, or the effect itself is 50% stronger.",
            "Crafting Insight":
                "You are inspired, and you finish crafting the object or structure earlier than was expected (maybe "
                "even halving the total time).",
            "Tinkering Vision":
                "When using your Always Tinkering special ability, you discover that the materials you’re using are "
                "of unexpectedly high quality, giving you specific options to choose from. So instead of gaining a "
                "random cypher, you gain the cypher of your choice (though it’s still a temperamental cypher, "
                "so it’s 2 levels lower than normal and you can’t give it to someone else without destroying it)."
        },
        "Starting Equipment": {
            "Equipment": ["clothing", "weapon a", "an explorer's pack", "a book about crafting",
                          "a box of crafting tools", "if you start with a ranged weapon: 12 of that ammunition"],
            "Shins": 5,
            "Cyphers": ["crafter’s eyes", "instant item", "gravity changer"],
            "Oddities": ["Piece of extremely strong and thin cable 8 feet (2.5 m) long"],
            "Iotum": {"io": 4, "responsive synth": 4},
            "Parts": 6
        },
        "Community Bonus": "",
        "Connections": [
            "Your mother praised your artistic talent as a child, but you chose to give it up in favor of crafting.",
            "You lost your brother when you were young. Your only memory of him is a doll you yet keep.",
            "You retain a pet automaton about the size of a breadbox with wheels that you had even as a child.",
            "You are known as a seller of strange gadgets and once even made your living doing so.",
            "You once created a machine for distilling spirits that your friends still tell stories about.",
            "You had a partner who also enjoyed crafting, but there was an accident and they died.",
            "You created a device that caused you to disappear for three months. You later reappeared with no memory "
            "of what had happened and a star-shaped scar on your left temple.",
            "You’re a member of a secret organization of wrights who occasionally share messages and plans.",
            "You once owned a plan for crafting a dread destroyer, but it was stolen.",
            "One of your creations accidentally triggered a local incident with the iron wind. At least, that’s what "
            "some accused you of after it was all over and the dead were counted. You don’t think it was your fault, "
            "but you wonder.",
            "You had an apprentice you were teaching your craft to, but they left you in the middle of your most "
            "important project, causing it to fail.",
            "Your best friend from your youth is now a hated outlaw, though others say they are a hero. You’re not "
            "sure where the truth lies.",
            "You once met the Amber Pope in Qi and received a verbal invitation to return one day.",
            "On a few occasions, you’ve found just the iotum you needed to proceed in your work. You don’t know who "
            "or what has been responsible for providing them.",
            "You were a member of the Convergence, until you thought better of it. You still know one or two members.",
            "Religion has always been part of your life, though only recently have you thought to question it.",
            "A great musician in a nearby large city claims they owe their success to an instrument you crafted.",
            "You know where dozens, perhaps even hundreds, of plan seeds are located, but you haven’t been able to "
            "mount an expedition to locate and secure the cache yet.",
            "You were accused of murdering your brother. You fled to where you are now.",
            "You were trained by a master wright who left the world in a magnificent starcraft they built.",
        ],
        "Tiers": {
            '1': {
                "Always Tinkering":
                    "If you have any tools and materials at all, and you are carrying fewer cyphers than your limit, "
                    "you can create a cypher if you have an hour of time to spend. The new cypher is random and "
                    "always 2 levels lower than normal (minimum 1). It’s also temperamental and fragile. These are "
                    "called temperamental cyphers. If you give it to anyone else to use, it falls apart immediately, "
                    "useless. Action to initiate, one hour to complete.",
                "Community Builder":
                    "While you are present within the community, and actively and personally working on behalf of "
                    "that community, +3 is added to the community’s infrastructure. Enabler.",
                "CHOOSE2": {
                    "Additional Numenera Plans":
                        "You gain two additional numenera plans. You can take this ability multiple times. Enabler.",
                    "Deconstruct (3 Intellect points)":
                        "You take the time to closely study a bit of scrap, machine, cypher, artifact, or other "
                        "numenera object or structure before attempting to salvage iotum from it. If the salvage "
                        "source possesses iotum that can be salvaged (as determined by the GM), the salvage task "
                        "gains an asset. In addition, you gain one additional iotum from the salvage attempt, "
                        "which means one additional roll on the Iotum Result Table. Action to initiate, ten minutes "
                        "to complete.",
                    "Extra Use":
                        "(3 Intellect points) You attempt to gain an extra use from an installation or artifact "
                        "without triggering a depletion roll. The difficulty of the task is equal to the level of the "
                        "installation or artifact. If you crafted the installation or artifact, you gain an asset to "
                        "the task. On a failure, the depletion roll occurs normally. You could also try to use a "
                        "cypher without burning it out, but the task is hindered. A failed attempt to gain an "
                        "additional use from a cypher destroys it before it can produce the desired effect. Action.",
                    "Natural Crafter":
                        "All commonplace objects or structures you craft are effectively 1 level higher than an "
                        "average example of that object or structure. For instance, if you craft a defensive wall "
                        "that would normally be level 4, its effective level is 5. Enabler.",
                    "Right Tool for the Job":
                        "(1 Intellect point + iotum) If you have at least 1 unit of iotum, you can fashion a "
                        "temporary device that  provides an asset to one physical, non- combat task, identified ahead "
                        "of time.  For example, if you need to climb a wall, you could create some sort of climbing "
                        "assistance device; if you need to break out of a cell, you can tune iotum in your possession "
                        "to serve as a lockpick; if you need to create a small distraction, you could trigger an "
                        "iotum to make a loud bang and flash; and so on. Once fashioned, the adapted iotum lasts for "
                        "about a minute or until used for the intended purpose. This use destroys the iotum. Action "
                        "to prepare the iotum; action to initiate.",
                    "Scan for Iotum":
                        "(2 Intellect points) Using a device or some kind of unique sense, you scan an area equal in "
                        "size to a 10-foot (3 m) cube, including all objects or structures. The area must be within "
                        "immediate range. The difficulty of the task is equal to the level of the object or structure "
                        "being scanned. Scanning in this fashion grants an asset to initial salvage tasks in the area "
                        "to determine if anything is worth salvaging. This ability doesn’t improve your ability to "
                        "find a specific kind of iotum, only to discover whether there is iotum within the salvage "
                        "source in the first place. That said, many materials and energy fields prevent or resist "
                        "scanning. Action.",
                    "Scramble Machine":
                        "(2 Intellect points) You render one machine within short range unable to function for one "
                        "round. Alternatively, you can hinder any action by the machine (or by someone attempting to "
                        "use the machine) for one minute. Action.",
                    "Trained in Armor":
                        "You can wear armor for long periods of time without tiring and can compensate for slowed "
                        "reactions from wearing armor. You can wear any kind of armor. You reduce the Speed Effort "
                        "cost for wearing armor by 1. If you choose this as one of your starting inspired techniques, "
                        "you start the game with armor of your choice. Enabler.",
                    "Trigger Iotum Ray":
                        "(1 Intellect point or iotum) If you have at least 1 unit of iotum,  you can trigger it to "
                        "release a short- range ray of force that inflicts 3 points of  damage. This does not destroy "
                        "the iotum. Alternatively, you can choose to have this destroy the iotum, in which case there "
                        "is no Intellect cost. Action.",
                }
            },
            '2': {
                "Numenera Plans":
                    "You gain two additional numenera plans of your choice. Enabler.",
                "CHOOSE1": {
                    "Additional Training":
                        "You are trained in two additional crafting skills of your choice. Enabler.",
                    "Boost Cypher (2 Intellect points)":
                        "The cypher you activate with your next action functions as if it were 2 levels higher. "
                        "Action.",
                    "Disable Machine (3+ Intellect points)":
                        "With a few deft touches, you infuse a powered device of level 3 or lower with conflicting "
                        "instructions. If affected, the device is destroyed or disabled for at least one minute, "
                        "depending on its size and complexity. The GM may rule that the disabling effect lasts until "
                        "the device is repaired. In addition to the normal options for using Effort, you can also "
                        "choose to use Effort to increase the maximum level of the target by 1 for each level "
                        "applied. Thus, to overload a level 5 device (two levels above the normal limit), you must "
                        "apply two levels of Effort. Action. ",
                    "Impressive Device":
                        "(3 Intellect points or iotum) If you have at least 1 unit of iotum, you can fashion a "
                        "temporary device that causes some kind of impressive visual or audio display, "
                        "such as colored lights that form a tracery over your entire body and change according to "
                        "your mood and desire. The effect lasts for one minute. During this period, "
                        "all your interaction tasks gain an asset. Once fashioned, the adapted iotum lasts for about "
                        "a minute or until used for the intended purpose. This does not destroy the iotum. "
                        "Alternatively, you can choose to have this destroy the iotum, in which case there is no "
                        "Intellect cost. Action to prepare the iotum; action to initiate.",
                    "Interaction Skills":
                        "You are trained in two skills in which you are not already trained. Choose two of the "
                        "following: deceiving, persuading, public speaking, seeing through deception, "
                        "or intimidating. You can select this ability multiple times. Each time you select it, "
                        "you must choose two different skills. Enabler.",
                    "Knowledge Skills":
                        "You are trained in two skills in which you are not already trained. Choose two areas of "
                        "knowledge such as history, geography, archeology, and so on. You can select this ability "
                        "multiple times. Each time you select it, you must choose two different skills. Enabler.",
                    "Make Do With Available Iotum":
                        "(3+ Intellect points) Given an hour or so, you can figure out a way to substitute one kind "
                        "of iotum called for in a plan with another kind of iotum, as long as the iotum you use is at "
                        "least 1 level higher than the iotum originally called for. Alternatively, you can make do "
                        "with 1 unit less than the number of units called for by the plan (to a minimum of 1 unit). "
                        "For each additional level of Effort you apply, you can reduce the number by an additional "
                        "unit, to a minimum of 1 unit. You can never substitute more than one kind of iotum per "
                        "individual crafting task, though you could simultaneously substitute an iotum and decrease "
                        "the number of units required by applying additional Effort. Action to initiate, one hour to "
                        "complete.",
                },
            },
            '3': {
                "Improved Community Builder":
                    "A community continues to gain +3 to infrastructure due to your influence. However, you do not "
                    "need to be constantly present in and actively working on behalf of the community for it to gain "
                    "this benefit; it gains it merely because of your past crafting work in the community. Enabler. ",
                "Expert Cypher Use":
                    "You can bear four cyphers at a time.",
                "Numenera Plans":
                    "You gain two additional numenera plans of your choice. Enabler.",
                "CHOOSE1": {
                    "Adept Builder":
                        "When you attempt a crafting task, you lower the assessed difficulty for creating a complex "
                        "object or structure by one step. For example, if the assessed difficulty for creating a "
                        "level 3 installation would normally be 6, for you the assessed difficulty is 5 (this also "
                        "reduces the crafting time). If you’re trained or specialized in a relevant crafting skill ("
                        "which you likely are), that could reduce the assessed crafting difficulty to 4 or 3, "
                        "also reducing the time to build even more. Enabler.",
                    "Community Awareness":
                        "(4 Intellect points) While you are within a community that currently benefits from your "
                        "Community Builder or Improved Community Builder ability, you can ask the GM a very simple, "
                        "general question about that general area, such as “Are there enemies trying to sneak over "
                        "the wall?” or “Is someone watching the flower shop?” or “Is there a Nano sensor active by my "
                        "home?” If the answer you seek is not in the area, you receive no information. Action.",
                    "Device Insight (3+ Intellect points)":
                        "When examining any numenera device, you can ask the GM one question about the device to gain "
                        "an idea of its capabilities or functions, how it can be activated or deactivated, "
                        "what its weakness is, how it can be repaired, or any other similar query. This ability is "
                        "for difficult or strange things beyond those readily identified by understanding numenera. "
                        "The GM may require a roll whose difficulty is equal to the device’s level; however, "
                        "you gain two assets to any such task, and training in the understanding numenera skill also "
                        "applies. Each time you use this ability on the same device after the first use, you must "
                        "apply one additional level of Effort. Action.",
                    "Follower":
                        "You gain a level 2 follower. One of their modifications must be for crafting, such as "
                        "crafting numenera. You can take this ability multiple times, each time gaining another "
                        "level 2 follower. Enabler.",
                    "Modify Cyphers":
                        "You can take any two cyphers and quickly jury-rig a new cypher of the same level as the "
                        "lowest-level cypher. You determine the function of the new cypher, but it must be that of a "
                        "cypher you have used before (but not necessarily one for which you have plans). The new "
                        "cypher is a temperamental cypher, like those created with your Always Tinkering ability. The "
                        "original two cyphers are consumed in this process. This ability does not function if one or "
                        "more of the original cyphers are temperamental. Action.",
                    "Quick Armoring":
                        "(4 Intellect points + io) You can siphon the residual energy in io (the eponymous iotum) to "
                        "integrate and reinforce a layer of tightly wrapped clothing or encompassing cloaks that you "
                        "wear. This requires at least one io, although it is not consumed in the process. For the "
                        "next hour, you gain +2 to Armor. Action to initiate, one minute to complete. ",
                    "Skill with Attacks":
                        "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                        "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, "
                        "or heavy ranged. You are trained in attacks using that type of weapon. You can select this "
                        "ability multiple times. Each time you select it, you must choose a different type of attack. "
                        "Enabler.",
                },
            },
            '4': {
                "Numenera Plans":
                    "You gain two additional numenera plans of your choice. Enabler.",
                "CHOOSE1": {
                    "Boost Artifact":
                        "(2 Intellect points) An artifact you activate with your next action functions as if it were "
                        "two levels higher. Action.",
                    "Confounding Jargon (4 Intellect points)":
                        "You begin to discuss the intricacies of crafting numenera, which goes completely over the "
                        "heads of most creatures but is sufficient to distract a target within immediate range until "
                        "your next turn. You and each of your allies gain an asset on one interaction, attack, "
                        "or defense task associated with the target before your next turn. This ability doesn’t work "
                        "on creatures you can’t talk with. Action.",
                    "Energy Redirection (5+ Intellect points)":
                        "You take the time to closely study a bit of scrap, machine, cypher, artifact, or other "
                        "numenera object or structure. When you’ve finished, you can drain the energy from it and "
                        "redirect it elsewhere. Iotum are burned out. Cyphers are rendered useless. Artifacts, "
                        "installations, vehicles, and automatons must make a depletion roll. You can redirect the "
                        "energy from the target object to restore 1 Might point per level of the target object. "
                        "Alternatively, you can redirect the energy into a depleted cypher, artifact, installation, "
                        "vehicle, or automaton that has a level equal to or less than the drained object. If the "
                        "device isn’t broken, it gains one additional use and then becomes depleted and broken. Each "
                        "additional level of Effort you apply increases the maximum level of the object you can "
                        "recharge. Action to initiate, ten minutes to complete.",
                    "Expert Crafter":
                        "Instead of rolling, you can choose to automatically succeed on a crafting task you’re "
                        "trained in. The task must be difficulty 4 or lower. If you are able to reduce the assessed "
                        "difficulty of a crafting task to 4 or lower, this ability also applies to each subtask, "
                        "assuming something doesn’t interrupt you during the ensuing time to build. Enabler. ",
                    "Knowing the Weak Points":
                        "You gain +3 damage when attempting to damage a device, automaton, or other machine. Enabler.",
                    "Machine Bond":
                        "From very long range, you can activate and control a device (including an installation, "
                        "automaton, or vehicle) that you have bonded with. For example, you can detonate a cypher "
                        "even when it is held by someone else, or cause an installation turret to fire where you "
                        "direct. Bonding is a process that requires 28 hours of meditation in the presence of the "
                        "machine. Action.",
                },
            },
            '5': {
                "Numenera Plans":
                    "You gain two additional numenera plans of your choice. Enabler.",
                "Master Cypher Use":
                    "You can bear five cyphers at a time.",
                "CHOOSE1": {
                    "Boost Cypher Function":
                        "(4 Intellect points) Add 3 to the functioning level of a cypher that you activate with your "
                        "next action, or change one aspect of its parameters (range, duration, area, etc.) by up to "
                        "double or down to one tenth. Action.",
                    "Faster Builder":
                        "When you attempt a crafting task, you lower the assessed difficulty for creating a complex "
                        "object or structure by two steps. (This replaces Adept Builder, if you took that; you can "
                        "exchange that ability for another tier 3 inspired technique.) Enabler.",
                    "Improved Follower":
                        "You gain a level 3 follower. They are not restricted on their modifications. You can take "
                        "this ability multiple times, each time gaining another level 3 follower. Alternatively, "
                        "you could choose to advance a level 2 follower you already have to level 3 and then gain a "
                        "new level 2 follower. Enabler.",
                    "Modify Artifact Function":
                        "(5 Intellect points) You can take an artifact and any two cyphers and quickly jury-rig a new "
                        "artifact of the level of the lowest-level cypher. You determine the function of the new "
                        "artifact, but it must be that of an artifact or cypher you have used before (but not "
                        "necessarily one for which you have plans). The GM sets the depletion of the new artifact, "
                        "if applicable (it will usually be a bit worse than the original artifact). The two cyphers "
                        "and the original artifact are consumed in this process. The original cyphers cannot be "
                        "temperamental cyphers. Action.",
                    "Modify Artifact Power (6 Intellect points)":
                        "You permanently add +1 to the level of an artifact of up to level 5. The difficulty of this "
                        "task is equal to the modified higher level of the artifact. If the task is failed, "
                        "the artifact makes a depletion roll and is not advanced in level. Once modified, "
                        "the artifact can’t be similarly boosted again. Action.",
                    "Quick Mind Boost":
                        "You can siphon the residual energy in a single iotum to enhance your Intellect Edge by +1 "
                        "for one minute. The iotum is destroyed. This ability does not allow you to enhance your Edge "
                        "by more than +1. Action.",
                    "Town Pride":
                        "While you’re in a community that currently benefits from your Community Builder or Improved "
                        "Community Builder special ability, your Might Edge, Speed Edge, and Intellect Edge all "
                        "increase by 1. When you make a recovery roll in this community, you recover twice as many "
                        "points. You can gain the benefit of this inspired technique even if you’re not in the "
                        "community, as long as you have visited within the last three days. Enabler.",
                },
            },
            '6': {
                "Numenera Plans":
                    "You gain two additional numenera plans of your choice. Enabler.",
                "Recruit Deputy":
                    "You gain a level 4 follower. They are not restricted on their modifications. Enabler.",
                "CHOOSE1": {
                    "Juggernaut":
                        "(9 Intellect points) You call upon your connection to one installation  you’ve built or "
                        "repaired to become a single- use weapon of immense destruction,  though this also destroys "
                        "the installation. While you are within a community that currently benefits from your "
                        "Community Builder or Improved Community Builder ability, you can select an installation of "
                        "level 5 or higher within very long range. The installation launches itself like a massive "
                        "missile at a target you specify within very long range of the installation and then "
                        "detonates, inflicting 20 points of damage on all targets within short range. This destroys "
                        "the installation. Targets who successfully defend still suffer 8 points of damage. Action.",
                    "Master Machine (8 Intellect points)":
                        "You can control the functions of a machine you have bonded with, including installations, "
                        "intelligent or otherwise. In addition, if you use an action to concentrate on a machine, "
                        "you are aware of what is going on around it (you see and hear as if you were standing next "
                        "to it, no matter how far away you are). You must touch the machine to create the bond, "
                        "but afterward, there is no range limitation. This bond lasts for one week. You can bond with "
                        "only one machine at a time. Action to initiate.",
                    "Rapid Builder":
                        "When you attempt a crafting task, you lower the assessed difficulty for creating a complex "
                        "object or structure by three steps. (This replaces Adept Builder and Faster Builder, "
                        "if you took either of those; you can exchange those abilities for another tier 3 and tier 5 "
                        "inspired technique.) Enabler.",
                    "Summon Sferic":
                        "(8+ Intellect points) A sferic appears within a few days after you construct a simple beacon "
                        "designed as a lure. If you apply an additional level of Effort as part of the call, "
                        "the sferic is amenable to your instructions toward building an object or structure; "
                        "otherwise, it acts according to its nature (which means it might still build something for "
                        "you, but you risk having your mind plucked from your head when you make your request). The "
                        "sferic remains until it finishes creating the structure you asked of it or it is attacked ("
                        "in which case it defends itself and then leaves). Action to initiate, three days to "
                        "construct beacon and summon sferic.",
                    "Usurp Cypher":
                        "Choose one cypher that you carry. The cypher must have an effect that is not instantaneous. "
                        "You destroy the cypher and gain its power, which functions for you continuously. You can "
                        "choose a cypher when you gain this ability, or you can wait and make the choice later. "
                        "However, once you usurp a cypher’s power, you cannot later switch to a different cypher—the "
                        "ability works only once. Action to initiate.",
                },
            }
        }
    },
    "Delve": {
        "Base Stats": [9, 9, 10],
        "Starting Edge": [0, 1, 1],
        "Weapon Proficiencies": ["Light", "Medium"],
        "Class Skills": ["Salvaging Numenera", "CHOICE:Exploration Skill"],
        "Cypher Limit": 2,
        "Class Intrusions": {
            "Fortuitous Malfunction":
                "A trap or a dangerous device malfunctions before it can affect you.",
            "Serendipitous Landmark":
                "Just when it seems like the path is lost, or you are, a trail marker, landmark, or simply the way "
                "the terrain or corridor bends, rises, or falls away suggests to you the best path forward, "
                "at least from this point.",
            "Weak Strain":
                "The poison or disease turns out not to be as debilitating or deadly as it first seemed, and inflicts "
                "only half the damage that it would have otherwise.",
        },
        "Starting Equipment": {
            "Equipment": ["clothing", "one weapon", "light armor or 1 extra unit of responsive synth(your choice)",
                          "a pack of light tools", "an explorer’s pack",
                          "If you start with a ranged weapon, 12 of that ammunition"],
            "Shins": 3,
            "Cyphers": ["Phasing Gloves", "Travel Bubble"],
            "Oddities": ["Shirt that displays your muscles, bones, and internal organs when you wear it"],
            "Iotum": {},
            "Parts": 0,
        },
        "Connections": [
            "You always seem to run into another delve when you explore. Sometimes they help, but sometimes they take "
            "the best a ruin has to offer and leave you with drit.",
            "A merchant in a nearby city is always asking you for rare and wondrous items, which you’re pretty sure "
            "they resell for a far higher price than they ever give you.",
            "One of your parents was a minor official, with access to many privileges and much information.",
            "Your sibling became a glaive and now serves with a traveling band of specimen collectors in the employ "
            "of some organization whose name you can never remember.",
            "Before becoming a full-time explorer, you sometimes sang in taverns for your meals. You even created a "
            "few songs that are still sung by other balladeers.",
            "The town you grew up in was destroyed in a disaster that involved a flock of brilliant spheres of light "
            "that burst from the earth and rose into the sky, each taking a portion of the town away.",
            "You were taken into slavery as a child but later escaped. You still have scars and bad dreams.",
            "The Amber Gleaners have been attempting to recruit you, but so far you’ve put them off.",
            "You owe money to a number of people and don’t have the funds to pay your debts. Nobody seems interested "
            "in taking iotum.",
            "You ran with bandits for a short period, but you left them after thinking better of it. Now, however, "
            "they are after you, swearing that no one leaves their group while still breathing.",
            "You taught children for many years, but those days are behind you now.",
            "As an orphan, you had a difficult childhood, and your entry into adulthood was challenging.",
            "You led a double life. Most people know you as a conscientious and daring explorer, but you led another "
            "life as a thrill-seeking thief. You don’t indulge much in the latter anymore, but you sometimes dream "
            "about your lost cache of “trophies.”",
            "You led a popular uprising in the town where you grew up, and you won. The old leaders were exiled.",
            "You were married, but your partner was stolen by transdimensional beings.",
            "The Order of Truth cut you from the ranks when you consistently failed to finish the tasks they set "
            "before you, but you claim it was because your supervisor failed to tell you what those tasks actually "
            "were.",
            "As an envoy working in a distant city, you made friends that you still miss today.",
            "You had a pet that you loved dearly, but it was killed in an accident. You’re still searching for how "
            "that accident came to be; could it have been a deliberate act by your enemies?",
            "You were best friends with a nano, possibly even lovers, but the iron wind took them away from you.",
            "You’ve often been maligned for your looks. Ungainly, different, of a different species or cultural "
            "background—the reason you look different than others is up to you.",
        ],
        "Tiers": {
            '1': {
                "Community Explorer":
                    "While you are present within a community, and actively and personally working on behalf of that "
                    "community, the community’s effective rank for purposes of finding resources, locating new trade "
                    "routes, knowing about conditions just beyond the community, and detecting sneak attacks by "
                    "enemies is +1. Enabler.",
                "CHOOSE2": {
                    "Additional Training":
                        "You are trained in two additional skills in which you are not already trained. Choose from the "
                        "following: navigation, perception, sensing danger, initiative, peacefully opening communications "
                        "with strangers, and tracking. Enabler.",
                    "Familiarize":
                        "You can familiarize yourself with a new area if you spend at least one hour studying a region up "
                        "to a long distance across that you are able to directly access and move about in. Once you’ve "
                        "familiarized yourself with an area, all your tasks related to perception, navigation, salvaging, "
                        "defense, and moving about the area gain an asset. Each time you familiarize yourself with a new "
                        "area, you lose focus on a previous area unless you spend 1 XP to retain the familiarity "
                        "permanently. Action to initiate, one hour to complete.",
                    "Find the Way":
                        "When you apply Effort to a navigation task because you don’t know the way, are lost, "
                        "are attempting to blaze a new route, need to choose between two or more otherwise similar paths "
                        "to take, or something very similar, you can apply a free level of effort. Enabler.",
                    "Right Tool for the Job":
                        "(1 Intellect point + iotum) If you have at least 1 unit of iotum, you can fashion a temporary "
                        "device that  provides an asset to a physical, non- combat task (identified ahead of time).  For "
                        "example, if you need to climb a wall, you could create some sort of climbing assistance device; "
                        "if you need to break out of a cell, you can tune iotum in your possession to serve as a "
                        "lockpick; if you need to create a small distraction, you could trigger an iotum to make a loud "
                        "bang and flash; and so on. Once fashioned, the adapted iotum lasts for about a minute or until "
                        "used for the intended purpose. This use destroys the iotum. Action to prepare the iotum; action "
                        "to initiate.",
                    "Skill With Defense":
                        "Choose one type of defense task in which you are not already trained: Might, Speed, "
                        "or Intellect. You are trained in defense tasks of that type. You can select this lore up to "
                        "three times. Each time you select it, you must choose a different type of defense task. Enabler.",
                    "Trained in Armor":
                        "You can wear armor for long periods of time without tiring and can compensate for slowed "
                        "reactions from wearing armor. You can wear any kind of armor. You reduce the Speed Effort cost "
                        "for wearing armor by 1. Enabler.",
                    "Trained Without Armor":
                        "You are trained in Speed defense tasks when not wearing armor. Enabler.",
                }},
            '2': {"CHOOSE1": {
                "Curious":
                    "You’re always curious about your surroundings, even on a subconscious level. Whenever you spend "
                    "Effort to attempt navigation, perception, or initiative tasks in an area that you’ve only rarely "
                    "or never visited before, you can apply an additional, free level of Effort. Enabler.",
                "Danger Instinct":
                    "(3 Speed points) If you are attacked by surprise, whether by a creature, a device, or simply an "
                    "environmental hazard (a tree falling on you), you can move an immediate distance before the "
                    "attack occurs. If moving prevents the attack, you are safe. If the attack can still potentially "
                    "affect you—if the attacking creature can move to keep pace, if the attack fills an area too big "
                    "to escape, etc.— the ability offers no benefit. Enabler.",
                "Environmental Adaptation":
                    "(2+ Intellect points) You use your wits and some learned tricks to survive a hostile "
                    "environment. You can breathe safely in smoke or poison gas or survive temperature extremes for "
                    "up to ten hours. In certain instances, the GM might require simple materials (like a bit of "
                    "cloth to cover your mouth or a cloak soaked in water to survive heat). In extreme cases, "
                    "such as crushing gravity or burning lava, this ability requires io, which are consumed after the "
                    "use. In these extreme environments, the GM might increase the cost of activating this ability to "
                    "equal the amount of damage you would sustain in a given round, split evenly between io and "
                    "Intellect. For example, if you enter a hostile environment that would normally deal 6 points of "
                    "damage per round, avoiding that damage would cost 3 io and 3 Intellect points. You can protect "
                    "other creatures in addition to yourself, but each additional creature costs you the same number "
                    "of io and Intellect points as it costs to protect you. Thus, if it costs 3 io and 3 points to "
                    "protect yourself, it costs 6 additional io and Intellect to protect two other people. In extreme "
                    "environments, this ability lasts for about a minute. This ability never protects against quick, "
                    "instantaneous threats, like an attack with a weapon or a sudden explosion of fire. Action to "
                    "initiate, unless io or elaborate materials are required, in which case action to initiate, "
                    "one minute to complete.",
                "Eye for Detail":
                    "(2 Intellect points) When you spend five minutes or so thoroughly exploring an area no larger "
                    "than a short distance in diameter, you can ask the GM one question about the area. The GM must "
                    "answer you truthfully. You cannot use this more than one time per area per 28 hours. Action to "
                    "initiate, five minutes to complete.",
                "Foil Danger":
                    "(2 Intellect points) You negate one source of potential danger related to one creature or object "
                    "that you are aware of within immediate distance for one round. This could be a weapon or device "
                    "held by someone, a trap triggered by a pressure plate, or a creature’s natural ability ("
                    "something special, innate, and dangerous, like an ithsyn’s gas spray or a cragworm’s venom). You "
                    "can also try to foil a foe's mundane action (such as an attack with a weapon or claw), "
                    "so that the action isn't made this round. Make your roll against the level of the attack, "
                    "danger, or creature. Action.",
                "Scorn Harm":
                    "You ignore the impaired condition and treat the debilitated condition as impaired. Enabler.",
                "Trapster":
                    "You are trained in creating simple traps for human-sized or smaller targets, especially many "
                    "varieties of deadfalls and snares using natural objects from the surrounding environment. When "
                    "you lay a trap, decide whether you want to hold the victim in place (a snare) or inflict damage "
                    "(a deadfall). Creating a snare is a difficulty 3 task, while the difficulty of creating a "
                    "deadfall is equal to the number of points of damage you want it to inflict. For example, "
                    "if you want to inflict 4 points of damage, that’s a difficulty 4 task (the training that comes "
                    "with this ability eases the task).  On a success, you create your one- use trap in about one "
                    "minute, and it is  considered level 3 for the purposes of avoiding detection before it is sprung "
                    "and for a victim trying to struggle free (if a snare). If you take one additional hour and use "
                    "additional resources equal to 10 io, the trap can instead be up to level 4, or level 5 if you "
                    "use additional resources equal to 20 io. Action to initiate, one minute or one hour to complete.",
            }},
            '3': {
                "Improved Community Explorer":
                    "A community continues to modify its rank by +1 on any task that involves finding resources, "
                    "locating new trade routes, knowing about conditions just beyond the community, and detecting "
                    "sneak attacks by enemies. However, you do not need to be constantly present in and actively "
                    "working on behalf of the community for it to gain this benefit; it gains it merely because of "
                    "your past efforts in the community. Enabler. ",
                "Expert Cypher Use":
                    "You can bear three cyphers at a time.",
                "CHOOSE1": {
                    "Creature Insight":
                        "(3 Intellect points) When examining any nonhuman creature, you can ask the GM one question "
                        "to gain an idea of its level, its capabilities, what it eats, what motivates it, "
                        "what its weaknesses are (if any), how it can be repaired, or any other similar query. This "
                        "is for difficult or strange creatures beyond those readily identified by using skills. "
                        "Action.",
                    "Device Insight":
                        "(3 Intellect points) When examining any numenera device, you can ask the GM one question to "
                        "gain an idea of its capabilities, how it functions, how it can be activated or deactivated, "
                        "what its weaknesses are (if any), how it can be repaired, or any other similar query. This "
                        "is for difficult or strange things beyond those readily identified by using the numenera "
                        "skill. Action.",
                    "Follower":
                        "You gain a level 2 follower. One of their modifications must be for salvaging numenera, "
                        "navigation, perception, sensing danger, initiative, or tracking. You can take this ability "
                        "multiple times, each time gaining another level 2 follower. Enabler.",
                    "Quick Wits":
                        "When performing a task that would normally require spending points from your Intellect Pool, "
                        "you can spend points from your Speed Pool instead. Enabler.",
                    "Resilience":
                        "You have 1 point of Armor against any kind of physical damage, even physical damage that "
                        "normally ignores Armor. Enabler.",
                    "Seize Opportunity":
                        "(4 Speed points) If you succeed on a Speed defense roll to resist an attack, you gain an "
                        "action, but the action is hindered. You can use your hindered action immediately even if you "
                        "have already taken a turn in the round. Using this ability doesn’t prevent you from taking "
                        "your normal action this round. Enabler.",
                    "Thinking Ahead":
                        "(variable Intellect points) You produce a remedy that removes a negative condition because "
                        "you’ve previously spent considerable time thinking ahead and preparing for your current "
                        "situation. For instance, if another character is poisoned, you produce an antidote, "
                        "or if they’re blinded, you produce a salve that returns sight (assuming they weren’t blinded "
                        "because their eyes were destroyed). The Intellect cost for using this ability is equal to "
                        "the level of effect or creature that caused the negative condition. Action.",
                    "Trapfinder":
                        "(3+ Intellect points) You find any traps (like a floor that would give way beneath you) or "
                        "mechanical triggers to a trap or defense system that might pose a threat. You can do this "
                        "without setting them off and in lieu of making a roll to find them. This ability can find "
                        "traps of level 4 or below. For each level of Effort you use, the level of traps that can be "
                        "found increases by 2, so a Delve using two levels of Effort can find all traps of level 8 or "
                        "below. Action.",
                    "Wrest From Chance":
                        "If you roll a natural 1 on a d20, you can reroll the die. If you reroll, you avoid a GM "
                        "intrusion—unless you roll a second 1—and might succeed on your task. Once you use this "
                        "ability, it is not available again until after you make a ten-hour recovery roll. Enabler. ",
                },
            },
            '4': {
                "Iotum Cache":
                    "Whenever you find or salvage iotum, you gain an additional result on the Iotum Result Table. "
                    "Enabler.",
                "CHOOSE1": {
                    "Counter Danger":
                        "(4 Intellect points) You negate a source of potential danger related to one creature or "
                        "object within immediate distance for one minute (instead of one round, as with Foil Danger). "
                        "This could be a weapon or device held by someone, a creature’s natural ability, "
                        "or a trap triggered by a pressure plate. You can also try to counter an action (like moving "
                        "or making a conventional, mundane attack with a weapon, a claw, etc.). Action.",
                    "Delve’s Fortitude":
                        "(4 Might points) If you are affected by an unwanted condition or affliction (such as "
                        "disease, paralysis, mind control, a broken limb, and so on—but not damage), you can ignore "
                        "it and act as if it does not affect you for one hour. You can use this ability to act as if "
                        "you were one step higher on the damage track for an hour— impaired becomes hale, debilitated "
                        "becomes impaired. If the condition would normally last less than an hour, it is entirely "
                        "negated. If you have a focus ability that grants this same benefit, you can ignore a "
                        "condition for five hours instead of one hour. Action.",
                    "Experienced Finder":
                        "(6+ Intellect points) When you are looking for something specific, such as a particular kind "
                        "of iotum, a chemical needed to complete a vaccine for a disease, a spare part required to "
                        "repair a damaged device, the tracks of a specific beast, or the sword that a thief stole "
                        "from you, this ability is of great use. For the next 28 hours, if you come within short "
                        "range of the thing and circumstances are such that it is possible for you to perceive the "
                        "thing (for example, it’s not in a locked chamber for which you do not have the key), "
                        "you find it. This ability assumes that you are constantly on the lookout, always looking "
                        "everywhere possible, peering behind obstacles, and so on—if you’re running for your life, "
                        "sleeping, or otherwise occupied, this ability does not help you. You use this ability in "
                        "lieu of making a roll to find the thing, but only if the difficulty for finding the object "
                        "is level 6 or below. You can apply Effort to increase the maximum level of the thing you’re "
                        "trying to find (each level of Effort used this way increases the maximum level by 1). "
                        "Enabler.",
                    "Greater Skill With Defense":
                        "Choose one type of defense task, even one in which you are already trained: Might, Speed, "
                        "or Intellect. You are trained in defense tasks of that type, or specialized if you are "
                        "already trained. You can select this lore up to three times. Each time you select it, "
                        "you must choose a different type of defense task. Enabler.",
                    "Skill With Attacks":
                        "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                        "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, "
                        "or heavy ranged. You are trained in attacks using that type of weapon. You can select this "
                        "ability multiple times. Each time you select it, you must choose a different type of attack. "
                        "Enabler.",
                    "Subtle Steps":
                        "When you move no more than a short distance, you can move without making a sound, regardless "
                        "of the surface you move across. Enabler.",
                },
            },
            '5': {
                "Adept Cypher Use":
                    "You can bear four cyphers at a time.",
                "Refine Iotum":
                    "When you discover iotum on an initial salvage task, your follow-up attempts to locate a specific "
                    "variety of iotum gain one free level of Effort if you use at least one level of Effort (maximum "
                    "six levels). Enabler.",
                "CHOOSE1": {
                    "Concussion":
                        "(5 Intellect points + iotum) If you have at least 1 unit of iotum, you can fashion a "
                        "concussive device. The adapted iotum can explode with concussive force, either after being "
                        "tossed up to a long distance or on a short timer, whichever you prefer. The explosion deals "
                        "5 points of damage to everything within short range. Even if you fail the attack roll, "
                        "targets in the area take 1 point of damage. Once fashioned, the adapted iotum lasts for "
                        "about a minute or until detonated. This use destroys the iotum. Action to tinker with the "
                        "iotum; action to initiate.",
                    "Free to Move":
                        "You ignore all movement penalties and adjustments due to terrain or other obstacles. You can "
                        "fit through any space large enough to fit your head. Tasks involving breaking free of bonds, "
                        "a creature’s grip, or any similar impediment gain three free levels of Effort. Enabler.",
                    "Group Friendship":
                        "(4 Intellect points) You convince a sentient creature to regard you (and up to ten creatures "
                        "that you designate within immediate distance of you) positively, as they would a potential "
                        "friend. Action.",
                    "Hard to Kill":
                        "You can choose to reroll any defense task you make but never more than once per round. "
                        "Enabler.",
                    "Improved Follower":
                        "You gain a level 3 follower. They are not restricted on their modifications. You can take "
                        "this ability multiple times, each time gaining another level 3 follower. Alternatively, "
                        "you can choose to advance a level 2 follower you already have to level 3 and then gain a new "
                        "level 2 follower. Enabler.",
                    "Numenera Adaptation":
                        "You have 2 points of Armor against any attack that comes from a numenera device, automaton, "
                        "or other mechanism. This is true even if the attack would normally ignore Armor. Enabler.",
                    "Vigilant":
                        "(5 Might points) When affected by an attack or effect that would daze or stun you, "
                        "you are not dazed or stunned. Enabler.",
                },
            },
            '6': {
                "Recruit Deputy":
                    "You gain a level 4 follower. They are not restricted on their modifications. Enabler.",
                "CHOOSE1": {
                    "Inspire Coordinated Actions":
                        "(9 Intellect Points) If your allies can see and easily understand you, you can instruct each "
                        "of them to take one specific action (the same action for all of them). If any of them choose "
                        "to take that exact action, they can do so as an additional action immediately. This doesn’t "
                        "interfere with them taking their normal actions on their turns. Action.",
                    "Mastery With Attacks":
                        "Choose one type of attack in which you are trained: light bashing, light bladed, "
                        "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, "
                        "or heavy ranged. You are specialized in attacks using that type of weapon. Enabler. (If you "
                        "aren’t trained in an attack, select Skill With Attacks to become trained in that attack.) ",
                    "Negate Danger":
                        "(7 Intellect points) You permanently negate a source of potential danger related to one "
                        "creature or object within immediate distance. This could be a weapon or device held by "
                        "someone, a creature’s natural ability, or a trap triggered by a pressure plate. Action.",
                    "Not Dead Yet":
                        "When you would normally be dead, you instead fall unconscious for one round and then awaken. "
                        "You immediately gain 1d6 + 6 points to restore your stat Pools, and you are treated as if "
                        "debilitated (if you also have Delve's Fortitude, you are only impaired) until you rest for "
                        "ten hours. If you die again before you take your ten-hour recovery roll, you are truly dead. "
                        "Enabler.",
                    "Share Defense":
                        "If your skill in a defense type is greater than that of an ally within short range, "
                        "your advice and insight can allow them to use your skill on that defense task. Enabler. ",
                },
            }
        }
    },
}

types = dict(discovery_types, **destiny_types)

descriptor_template = {
    "Stat Bonuses": [0, 0, 0],
    "Skills": [],
    "Inabilities": [],
    "Features": {},
    "Additional Equipment": {},
    "Link to Starting Adventure": []
}

discovery_descriptors = {
    "Charming": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Positive Interactions", "Abilities that Influence the Minds of Others"],
        "Inabilities": ["Tasks Involving Lore, Knowledge, or Understanding", "Resisting Mental Attacks"],
        "Features": {"Contact": "You have an important contact who is in an influential position, such as a minor"
                                " noble, the captain of the town guard, an Aeon Priest, or the head of a large gang of"
                                " thieves."},
        "Additional Equipment": {
            "Shins": 10
        },
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
        "Additional Equipment": {
            "Shins": 10,
        },
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
        "Additional Equipment": {},
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
        "Additional Equipment": {},
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
        "Additional Equipment": {
            "Equipment": ["Two books on topics of your choice"]
        },
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
        "Additional Equipment": {
            "Oddities": ["An Oddity, as determined by the GM"],
        },
        "Link to Starting Adventure": ["A dream guided you to this point.", "You need money to fund your studies.",
                                       "You believed the mission would be a great way to learn more about the numenera.",
                                       "Various signs and portents led you here."]
    },
    "Mechanical": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Understanding Numenera"],
        "Inabilities": ["Charm", "Persuasion", "Deception"],
        "Features": {"Sense 'Magic'": "You can sense whether the numenera is active in situations where its presence is"
                                      "not obvious. You must study an object or location closely for a minute to get a "
                                      "feel for whether the touch of the ancients is at work.",
                     "Esotry: Hedge Magic": "You can perform small tricks: temporarily change the color or basic "
                                            "appearance of a small object, cause small objects to float through the "
                                            "air clean a small area, mend a broken object, prepare (but not create) "
                                            "food, and so on. You can’t use Hedge Magic to harm another creature or "
                                            "object. Action."},
        "Additional Equipment": {
            "Oddities": ["An Oddity, as determined by the GM"],
        },
        "Link to Starting Adventure": ["A dream guided you to this point", "You need money to fund your studies",
                                       "You believed the mission would be a great way to learn more about the numenera",
                                       "Various signs and portents led you here"]
    },
    "Rugged": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": ["Climbing", "Jumping", "Running", "Swimming", "Training Natural Animals", "Riding Natural Animals",
                   "Placating Natural Animals", "Identifying and Using Natural Plants"],
        "Inabilities": ["Charm and Persuasion", "Etiquette", "Deception"],
        "Features": {},
        "Additional Equipment": {
            "Equipment": ["An Explorer's Pack"]
        },
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in your "
                                       "best interest.", "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Stealthy": {
        "Stat Bonuses": [0, 2, 0],
        "Skills": ["Stealthy Tasks", "Lies and Trickery", "Abilities involving Lies or Trickery"],
        "Inabilities": ["Movement-Related Tasks"],
        "Features": {},
        "Additional Equipment": {},
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
        "Additional Equipment": {
            "Equipment": ["Extra Medium or Heavy Weapon"],
        },
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
        "Additional Equipment": {},
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
        "Additional Equipment": {},
        "Link to Starting Adventure": ["Against your better judgment, you joined the other PCs because you saw that "
                                       "they were in danger.",
                                       "One of the other PCs convinced you that joining the group would be in your"
                                       " best interest.", "You’re afraid of what might happen if the other PCs fail.",
                                       "There is reward involved, and you need the money."]
    },
    "Tough": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": ["Might Defense"],
        "Inabilities": [],
        "Features": {"Resilient": "Armor + 1", "Healthy": "Add 1 to your recovery rolls"},
        "Additional Equipment": {"Equipment": ["Extra Light Weapon"]},
        "Link to Starting Adventure": ["You’re acting as a bodyguard for one of the other PCs.",
                                       "One of the PCs is your sibling, and you came along to watch out for them.",
                                       "You need money because your family is in debt.",
                                       "You stepped in to defend one of the PCs when they were threatened. While "
                                       "talking to them afterward, you heard about the group’s task."]
    },  # End Discovery Descriptors, Begin Destiny Descriptors
}

destiny_descriptors = {
    "Adaptable": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": ["Pleasant Social Interactions"],
        "Inabilities": [],
        "Features": {
            "Versatile":
                "+2 to any one Pool, which you can reassign after each ten-hour recovery roll.",
            "Resilient":
                "You’re trained in all actions that involve overcoming or ignoring the effects of deprivation, "
                "sorrow, or pain. This includes tasks related to ending an ongoing condition such as being dazed, "
                "blinded, stunned, and so on. (However, you are not trained in tasks to resist effects that confer "
                "those conditions in the first place.)",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "The other PCs were impressed by how quickly you adapted to a bad situation and invited you to join them.",
            "The other PCs were looking for someone else, but you convinced them that you were the perfect person to "
            "join them instead.",
            "The other PCs were in a bind, but you were able to convince a third party to let the PCs go about their "
            "business—and you with them.",
            "One of the other PCs used to remark on your adaptability when you were younger, and now they’ve asked "
            "you to come along on a new outing where your skills are likely to be useful.",
        ],
    },
    "Articulate": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Persuasion", "Plans (making and convincing others of them)"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "One of the other PCs asked you to explain something to them. Impressed, they asked you to accompany them "
            "on a mission.",
            "You were delighted with one of the other PCs’ ability to convey their ideas and asked to come along.",
            "You’ve made some enemies despite—or perhaps because of—your articulate nature, and you need to find "
            "friends or, better yet, leave the area for a while.",
            "Another PC asked you to take part in the mission because they felt it would fail without you.",
        ],
    },
    "Beneficent": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Pleasant Social Interaction", "putting other people at ease", "gaining others’ trust"],
        "Inabilities": [],
        "Features": {
            "Devoted":
                "Allies who have spent the last day with you add +1 to their recovery rolls. You also gain this "
                "benefit if at least one other ally gains it.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "Even though you didn’t know most of the other PCs beforehand, you invited yourself on their quest to "
            "help them.",
            "You saw the other PCs struggling to overcome a problem and selflessly joined them to help.",
            "You’re nearly certain the other PCs will fail without you.",
            "You had to choose between living your tattered life and helping others. You haven’t looked back since.",
        ],
    },
    "Cheerful": {
        "Stat Bonuses": [0, 0, 4],
        "Skills": ["CHOICE:A Hobby", "Making Friends", "Ending Conflicts", "Making a Positive First Impression"],
        "Inabilities": ["Detecting Falsehoods and Disguises"],
        "Features": {},
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "One of the other PCs asked you to come along because of your pleasant nature in the hopes that it would "
            "help bond the group.",
            "You were just trying to be agreeable, but you ended up agreeing to go on a mission.",
            "You woke up with a great idea for an expedition and got the other PCs to join you.",
            "Your cheerfulness saved you from violence when bad elements confronted you. Instead of beating you (or "
            "worse), they told you about something that led to your mission.",
        ],
    },
    "Civic": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Finding out Current Events and Secrets in your Community", "Aiding A Community"],
        "Inabilities": [],
        "Features": {
            "Civic-Minded":
                "You add +1 to the health of any community you are currently living in.",
        },
        "Additional Equipment": {"Plans": ["A Numenera Plan for Installation"]},
        "Link to Starting Adventure": [
            "While picking up litter around the community, you overheard the other PCs talking about a mission and "
            "asked to join.",
            "You need resources and friends to help you in your civic aspirations later.",
            "It was clear that the mission couldn’t succeed without your civic skills and knowledge.",
            "You thought the community would be endangered if you didn’t come along.",
        ],
    },
    "Committed": {
        "Stat Bonuses": [4, 0, 0],
        "Skills": ["Enduring Trials of Mind and Body"],
        "Inabilities": ["Persuasion"],
        "Features": {
            "Dedication Brings Rewards":
                "You tend to practice things over and over. Once between each ten-hour recovery roll, you gain an "
                "asset to similar actions involving the same task (such as making attacks against the same foe or "
                "operating the same device). The asset doesn’t apply to similar but different tasks (such as "
                "attacking a different foe, even if of the same kind, or operating a different but very similar "
                "device).",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "Your commitment to your cause seems to overlap some aspect of what the other PCs want to accomplish.",
            "You were looking for something to commit to, and the other PCs had a job they needed to get done.",
            "Obviously, a task like what the PCs had in mind needed someone as committed as you to see it through.",
            "As you completed another mission with great success, you overheard the other PCs talking about a new "
            "mission and asked to join.",
        ],
    },
    "Confident": {
        "Stat Bonuses": [1, 1, 1],
        "Skills": ["Non-Combat Non-Physical Skill A", "Non-Combat Non-Physical Skill B",
                   "Non-Combat Non-Physical Skill C"],
        "Inabilities": [],
        "Features": {
            "Confident Outlook":
                "Sometimes confidence counts as much as or more than competence. When you set your mind to it, "
                "you are trained in one task for ten minutes, as long as that task is not an attack or a defense. You "
                "can do this once per rest (the ability is renewed each time you make a recovery roll).",
            "Failure Has Its Consequence":
                "Sometimes confidence leads to overconfidence and a stark realization of failure. You trigger a GM "
                "intrusion on a d20 roll of 1 or 2.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You dragged one of the other PCs into it, certain that together you could accomplish anything.",
            "When the other PCs asked for help, you were confident that you could provide whatever was necessary.",
            "How could you not be involved? The mission requires someone with your skills to succeed.",
            "You told another PC that you’ve never failed and probably never would. They took you at your word and "
            "brought you along.",
        ],
    },
    "Cultured": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": ["Knowledge of Current Events", "History", "Perception", "Detecting Differences",
                   "Noticing Minor Flaws and Strengths in the Work of Others"],
        "Inabilities": ["Getting the Uncultured to Believe or Trust You"],
        "Features": {
            "Learned":
                "Being well read and well educated, you have a wide range of talents. You can attempt one task in "
                "which you have no training as if you were trained. This ability refreshes every time you make a "
                "recovery roll, but the uses never accumulate.",
        },
        "Additional Equipment": {
            "Equipment": ["a book on a topic of your choice", "a set of very fine clothing"],
        },
        "Link to Starting Adventure": [
            "You could see that the other PCs would fail without your help.",
            "You convinced one of the other PCs that you had invaluable skills.",
            "You know that expanding your education requires experience as well as study, and you believe that you "
            "can learn a lot by joining the other PCs.",
            "Just because you’re cultured doesn’t mean you don’t wish to explore, see new places, and make a name for "
            "yourself!",
        ],
    },
    "Curious": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Perception", "Detecting Falsehoods, Piercing Illusions or Disguises, and Seeing Past Facades"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": {"Equipment": ["three books on whatever subjects you choose"]},
        "Link to Starting Adventure": [
            "You were curious about what the PCs were doing and followed them.",
            "You heard that the other PCs were going someplace new and begged to go along.",
            "You got in over your head pursuing something fascinating, and the other PCs rescued you.",
            "One of the other PCs fascinates you, perhaps due to a special or weird ability they have.",
        ],
    },
    "Earnest": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Persuasion", "CHOICE:An Area of Lore or Knowledge", "Defence Rolls Against Disease and Poison",
                   "Providing Consolation or Emotional Support to Others"],
        "Inabilities": ["Seeing Through Lies or Trickery"],
        "Features": {},
        "Additional Equipment": {
            "Equipment": ["a friend has given you an additional expensive item worth up to 10 shins."]
        },
        "Link to Starting Adventure": [
            "Another PC told you what they were up to, and you joined them.",
            "Hard times overwhelmed you, and having no funds, you joined the other PCs.",
            "It was either join the other PCs or be kidnapped into a far worse situation.",
            "You suspect that the other PCs won’t succeed without you.",
        ],
    },
    "Empirical": {
        "Stat Bonuses": [0, 0, 4],
        "Skills": ["All actions related to conducting tests to find proof, discern the truth, or glean information"],
        "Inabilities": [],
        "Features": {
            "Quick Study":
                "When you take a round to study whatever is in front of you and gain the facts, you feel more "
                "confident that you’re about to do the right thing. Your next non-combat action gains an asset.",
            "Non-Resilient":
                "If you haven’t had time to study something, you have a hard time taking action and moving forward. "
                "Whenever you receive a GM intrusion, any action you take in response is hindered.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You’ve been studying a topic for a long time, and you think one of the other PCs has some knowledge "
            "about said topic.",
            "You need to gather some additional materials for something you are studying, and joining the other PCs "
            "seemed like a good way to get it.",
            "Someone told you an impossible story about this area, and you absolutely need to see for yourself to "
            "prove them wrong (or begrudgingly let them know they’re right).",
            "You recently read something that suggested there was more knowledge in the world than could be found in "
            "study. You’d like to find out if that is true.",
        ],
    },
    "Exacting": {
        "Stat Bonuses": [4, 0, 0],
        "Skills": ["Persuasion", "Intimidation", "Detecting Falsehoods"],
        "Inabilities": ["Positive Social Interactions", "Intellect Defence Rolls"],
        "Features": {},
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "The other PCs demonstrated they could meet your standards, and you offered to accompany them.",
            "Another PC helped you out of a difficult situation, and you accompanied them to repay the debt.",
            "Most people aren’t even worth considering, but the other PCs show promise.",
            "To tell the truth, being exacting all the time also leads to loneliness. You joined the other PCs "
            "because you wanted some company.",
        ],
    },
    "Forward-Thinking": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Initiative Tasks", "Leveraging Risk (Elements of Chance)"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": {"Shins": 30},
        "Link to Starting Adventure": [
            "A new danger arose, but you were prepared and responded with a pre-planned contingency.",
            "You showed up when and where you did after due consideration and forethought.",
            "In order to gain the resources you need for some longer-term projects, you need to accomplish "
            "shorter-term goals.",
            "You told one of the other PCs that nothing could surprise you because you’re always thinking ahead. They "
            "brought you along to test your claim.",
        ],
    },
    "Gregarious": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": [],
        "Inabilities": [],
        "Features": {
            "People Person":
                "When you are within immediate range of at least two allies, the difficulty of one non-combat-related "
                "task is eased. You can do this only once, but its use is restored each time you make a recovery roll.",
            "Getting the Word":
                "If you spend an hour amid a large group of people, you can glean general rumors, gossip, or opinions "
                "they hold.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You asked around and learned the other PCs were doing something interesting.",
            "You bought the other PCs a round of drinks, and they welcomed you into their ranks.",
            "You gathered the other PCs together for the task at hand.",
            "Doing anything is better than being alone.",
        ],
    },
    "Heroic": {
        "Stat Bonuses": [2, 0, 0],
        "Skills": ["All Social Interactions", "Perception", "Finding Hidden Things"],
        "Inabilities": ["Detecting Falsehoods"],
        "Features": {
            "Hero’s Complication":
                "Although the GM can use GM intrusions on you normally (awarding XP), they can also introduce a GM "
                "intrusion on you as if you had rolled a 1 on a d20 roll (without awarding XP) based on how your "
                "heroic nature tends to attract danger. Every other time the GM uses this ability to introduce a GM "
                "intrusion without giving you XP, your heroic nature works to your advantage. Your weapon breaks, "
                "but that allows you to notice something everyone else missed. A trap catches you, but it also "
                "catches your enemies. A new foe enters the fray, but your current foe mistakes it for your ally and "
                "attacks it instead of you. You and the GM should determine the advantage together.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You were hunting a great foe and hired the other PCs to accompany you.",
            "The PCs were looking for someone like you to round out their number.",
            "A mentor recommended you to the other PCs.",
            "You killed a mighty foe, and the other PCs were aided (or rescued from captivity) by that act.",
        ],
    },
    "Imaginative": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["CHOICE: An Artistic Skill", ],
        "Inabilities": [],
        "Features": {
            "Imaginative Solution":
                "When you apply a level of Effort to any Intellect task, you gain a free level of Effort. You can do "
                "this one time, although the ability is renewed each time you make a ten-hour recovery roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "In your head, the only way the group would succeed is if you were with them to save the day.",
            "You needed money, and this seemed like a good way to earn some.",
            "Experience is the best ingredient for even better panoramas of imagination.",
            "It sounded like fun.",
        ],
    },
    "Industrious": {
        "Stat Bonuses": [0, 4, 0],
        "Skills": [],
        "Inabilities": ["All Movement-Related Tasks"],
        "Features": {
            "Ready for What’s Next":
                "You add +1 to your recovery rolls.",
            "Imaginative Solution":
                "When you apply a level of Effort to any Intellect task, you gain a free level of Effort. You can do "
                "this one time, although the ability is renewed each time you make a ten-hour recovery roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "Following your plan got you to this point.",
            "Industry requires resources, and this mission seemed likely to provide what you needed.",
            "You believed the mission would be a great way to learn more about some of the roadblocks that stand in "
            "the way of achieving your goal.",
            "One of the other PCs said they’d help you if you helped them.",
        ],
    },
    "Intimidating": {
        "Stat Bonuses": [0, 0, 0],  # technically, choice of [2,0,0], [0,0,2], or [1, 0, 1]
        "Skills": ["Intimidation"],
        "Inabilities": ["Lore and Knowledge"],
        "Features": {
            "Threatening":
                "+2 to your Might Pool or +2 to your Intellect Pool or +1 to both Pools.",
            "Threaten":
                "Foes within immediate distance hesitate, which hinders their next action. You can do this once, "
                "although the ability is renewed each time you make a recovery roll.",
            "Menace":
                "One foe you choose within immediate range uses their next action to move away from you. You can do "
                "this once, although the ability is renewed each time you make a recovery roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You saw that the other PCs were in trouble and moved in on your own to see what was going on.",
            "You heard rumors that the other PCs were doing something interesting or profitable.",
            "One of the other PCs is a childhood friend of yours.",
            "One of the other PCs hired you to be a bodyguard.",
        ],
    },
    "Intuitive": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Perception"],
        "Inabilities": [],
        "Features": {
            "Know What to Do":
                "You can act immediately, even if it’s not your turn. Afterward, on your next regular turn, "
                "any action you take is hindered. You can do this one time, although the ability is renewed each time "
                "you make a recovery roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You just knew you had to come along.",
            "You convinced one of the other PCs that your intuition is invaluable.",
            "You felt that something terrible would happen if you didn’t go.",
            "You’re confident the reason you arrived at this point will soon become clear.",
        ],
    },
    "Irrepressible": {
        "Stat Bonuses": [4, 0, 0],
        "Skills": ["Positive Social Interaction"],
        "Inabilities": ["Intellect Defense to Trickery"],
        "Features": {
            "Bounces Back":
                "You add +1 to your recovery rolls.",
        },
        "Additional Equipment": [],
        "Link to Starting Adventure": [
            "The other PCs needed someone like you to keep them on track.",
            "One of the other PCs is a good friend or relation, and you wanted to look after them.",
            "Your last situation didn’t turn out as you had hoped, so you’re looking for a new direction.",
            "How hard can it be?",
        ],
    },
    "Lawful": {
        "Stat Bonuses": [2, 0, 0],
        "Skills": ["Knowing, Understanding, and Interpreting the Laws of the Land"],
        "Inabilities": ["Intellect Tasks while Law-breaking"],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": [
            "You heard what the other PCs were up to and knew they could use your expertise.",
            "You gathered the other PCs together to accomplish a lawful task.",
            "You agreed to provide money for the upkeep of an organization you are or were previously affiliated with "
            "and find yourself in need of new funds, so you joined the other PCs.",
            "You think the other PCs will help you bring law to areas that suffer lawlessness, once you get them on "
            "board with your way of thinking.",
        ],
    },
    "Loyal": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": [],
        "Inabilities": ["Detecting Falsehoods and Seeing Through Disguises"],
        "Features": {
            "Devoted":
                "If an ally within immediate range descends one step on the damage track, you can act immediately but "
                "in a restricted fashion. You can use this action either to move the willing ally up to an immediate "
                "distance or to attempt a healing task on your ally.",
            "Faithful":
                "When you help a creature to make or avoid an attack in combat, you regain 1 point to one of your "
                "Pools (this is true whether the task you helped with succeeds or fails). You can do this one time, "
                "although the ability renews each time you make a recovery roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "One of the other PCs needed help, and you obliged without a second’s hesitation.",
            "The other PCs were going somewhere, and you came along even though they didn’t ask you to.",
            "The other PCs thought you’d bring some much-needed grounding and connection for the team.",
            "You decided that the institution that previously commanded your loyalty wasn’t worthy of you, so you "
            "joined up with the other PCs.",
        ],
    },
    "Meddlesome": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Perception", "Detecting Falsehoods", "Stealth", "Remembering Details you've Read or Heard"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": [],
        "Link to Starting Adventure": [
            "You noticed that strange noises were coming from an abandoned area, so you gathered the other PCs to "
            "check it out.",
            "One of your mutual friends has gone missing, and you and the other PCs are determined to find them.",
            "You believed that the other PCs’ task might lead to important and maybe even amazing discoveries.",
            "Frightened by something, you fled to safety, but you returned with the other PCs to watch your back.",
        ],
    },
    "Nurturing": {
        "Stat Bonuses": [2, 0, 0],
        "Skills": ["Healing"],
        "Inabilities": [],
        "Features": {
            "Nurturing":
                "Allies who have spent the last day with you add +1 to their recovery rolls. You also gain this "
                "benefit if at least one other ally gains it.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You saw that one of the other PCs was hurt, so you offered your aid.",
            "You thought you heard someone crying out in need. When you investigated, you found the other PCs.",
            "You believed that the other PCs’ task could end up helping a huge number of people.",
            "You’d helped someone else until they no longer needed your care. So you went looking for someone or "
            "something new to nurture.",
        ],
    },
    "Obsessive": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": [],
        "Inabilities": [],
        "Features": {
            "Your Obsession":
                "At the beginning of each day, choose one concept on which you will concentrate. For the rest of that "
                "day, you’re obsessed with that concept. This doesn’t mean you ignore anything not related to your "
                "obsession. It just means you are at your best when performing tasks related to the obsession, "
                "and you are slightly inattentive when performing tasks that are not.",
            "Enthralled":
                "When you attempt a non-combat task that is directly related to your current obsession, you gain an "
                "asset. The player and GM can decide whether a particular situation warrants this benefit.",
            "Preoccupied":
                "Any task that is not related to your current obsession is hindered. The player and GM can decide "
                "whether a particular situation warrants this disadvantage.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You wouldn’t take no for an answer when you asked the other PCs if you could join their mission.",
            "You were preoccupied with something else and didn’t realize what you’d agreed to until it was too late.",
            "You believed that you could learn a lot by joining the other PCs.",
            "One of the other PCs asked you to come along, believing that your obsessive nature would be invaluable "
            "to the mission.",
        ],
    },
    "Optimistic": {
        "Stat Bonuses": [0, 0, 4],
        "Skills": ["Intellect Defence", ],
        "Inabilities": ["Might Defence", "Movement"],
        "Features": {
            "Shrugs Off Disappointment":
                "When you fail at a non-combat task and try that task again the very next round, you can apply a free "
                "level of Effort toward the success of that task. This benefit effectively alleviates the requirement "
                "to apply a level of Effort when retrying failed tasks.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "The PCs were in a bad spot, and one of the other PCs asked you along to add some perspective.",
            "You had a spot of bad luck, but you jumped back in to try something new, hopeful it would work out.",
            "To make good on a promise to help, you came with the other PCs.",
            "You answered a cry for help when another PC got in over their head.",
        ],
    },
    "Organized": {
        "Stat Bonuses": [0, 0, 4],
        "Skills": ["Perception", "Planning", "Organizing", ],
        "Inabilities": ["Intellect Defence in Messy or Chaotic Locations"],
        "Features": {
            "Benefits of Organization":
                "You can take one additional free action while you are at a location that you have organized to your "
                "liking (which means having spent at least ten minutes there tidying and organizing) or if you are "
                "following a plan that hasn’t diverged from the original conception. You can do this only once, "
                "but its use is restored each time you make a ten-hour recovery roll.",
        },
        "Additional Equipment": {"Equipment": ["an explorer's pack with extra pockets and compartments"]},
        "Link to Starting Adventure": [
            "You could tell from a distance that the other PCs needed your skills.",
            "The other PCs came to you looking for help with a plan of action.",
            "Things fell through, and going with the other PCs was your backup plan.",
            "There wasn’t a lot of call for neatness where you came from, which brought you to your current point.",
        ],
    },
    "Passionate": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": ["Running", "Climbing", "Swimming"],
        "Inabilities": ["Tasks that require restraint or subtlety, including sneaking or lying"],
        "Features": {
            "Fever":
                "You are a devil when angered, inflicting 1 additional point of damage with any attack.",
            "Fire Inside":
                "You gain one asset to an action when doing so can be justified by your passion. You can do this only "
                "once, but its use is restored each time you make a recovery roll.",
        },
        "Additional Equipment": [],
        "Link to Starting Adventure": [
            "You are madly in love with one of the other PCs and will do anything for them.",
            "The mission the other PCs were planning seemed vital to you for your own reasons. They had no choice but "
            "to let you get involved.",
            "You were guided to the other PCs and their task by someone you deeply respect.",
            "You’re looking for a cause worthy of you and your skills.",
        ],
    },
    "Persevering": {
        "Stat Bonuses": [0, 0, 0],  # Choice between intellect and Might
        "Skills": ["Endurance", "Persevering"],
        "Inabilities": [],
        "Features": {
            "Determined":
                "+2 to your Intellect Pool or +2 to your Might Pool.",
            "Irrepressible Reaction":
                "Whenever you receive a GM intrusion (either by rolling a 1 or by getting one from the GM), one "
                "action you take in response within the next minute gains an asset.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "By sticking with a difficult situation, you found the other PCs already involved in a task that you "
            "joined.",
            "Sometimes persevering means starting over when things don’t work out, and that’s how you found the other "
            "PCs.",
            "The other PCs earned your respect by accomplishing a difficult task in the face of many challenges.",
            "The other PCs said their mission would be difficult to complete, so you signed up to help.",
        ],
    },
    "Prepared": {
        "Stat Bonuses": [0, 4, 0],
        "Skills": ["Initiative"],
        "Inabilities": [],
        "Features": {
            "Tool Aficionado":
                "If a tool enables a non- combat task but does not provide an asset,  you gain an asset to that task "
                "anyway when using a tool. If a tool provides an asset to a non-combat task, you gain one additional "
                "asset when using it",
            "Inflexible":
                "You’re not usually surprised, so it’s extra surprising when you are. The first action you take after "
                "being surprised or when a foe attacks you before you have acted is hindered.",
        },
        "Additional Equipment": {"Equipment": ["a bag of light tools"]},
        "Link to Starting Adventure": [
            "You could tell the other PCs weren’t bringing the right tools for the job, so you offered to help.",
            "For someone as prepared as you are, having friends to help you is just common sense.",
            "When all your preparations came to nothing, you had nothing left but to strike out on your own, which "
            "is when the other PCs found you.",
            "The other PCs asked you to help them get ready for an important journey, and you ended up going with "
            "them.",
        ],
    },
    "Protective": {
        "Stat Bonuses": [0, 0, 4],
        "Skills": ["Perception", "Healing"],
        "Inabilities": ["Knowledge-Based Tasks"],
        "Features": {
            "Step in Front":
                "If you successfully draw the attack so that a foe attacks you instead of the target they originally "
                "intended to attack, you have +2 Armor against that attack. You can do this one time, although the "
                "ability renews each time you make a recovery roll.",
        },
        "Additional Equipment": [],
        "Link to Starting Adventure": [
            "You protected another PC from a bad situation, and now you’re friends.",
            "You thought that, without you, the other PCs would be in too much danger, and you offered to come along.",
            "The other PCs sought you out because of your reputation for helping others.",
            "You believed that by coming along with the other PCs, you would learn something that would help you "
            "protect an entire community later on.",
        ],
    },
    "Relentless": {
        "Stat Bonuses": [4, 0, 0],
        "Skills": ["Healing", "Finding Food and Water"],
        "Inabilities": ["Social Interaction"],
        "Features": {
            "Survivor’s Intuition":
                "You can come up with a random piece of information pertinent to the current situation when you wish. "
                "It is always an objective fact and must be something you could have logically read or seen in the "
                "past. You can do this one time, although the ability renews each time you make a ten-hour recovery "
                "roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "You found the other PCs in trouble and decided to help.",
            "Uncharacteristically, you were caught in a bind. The other PCs helped to free you.",
            "It was either do what needed doing or die. Now, here you are along with the other PCs.",
            "To protect a loved one, you agreed to join the other PCs because their quest was related to your own.",
        ],
    },
    "Risk-taking": {
        "Stat Bonuses": [0, 4, 0],
        "Skills": ["Leveraging Risk"],
        "Inabilities": ["Sneaking or Staying Quiet"],
        "Features": {
            "Pressing Your Luck":
                "You can choose to automatically succeed on one task without rolling, as long as the task’s "
                "difficulty is no higher than level 6. When you do so, however, you also trigger a GM intrusion as if "
                "you had rolled a 1. The intrusion doesn’t invalidate the success, but it probably qualifies it in "
                "some fashion. You can do this one time, although the ability renews each time you make a ten-hour "
                "recovery roll.",
        },
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "It seemed like there were equal odds that the other PCs wouldn’t succeed, which sounded good to you.",
            "You think the tasks ahead will present you with unique and fulfilling challenges.",
            "One of your biggest risks failed to go your way, and you need money to help pay that debt.",
            "You bragged that you never saw a risk you didn’t like, which is how you reached your current point.",
        ],
    },
    "Serene": {
        "Stat Bonuses": [0, 0, 2],
        "Skills": ["Intellect Defence", "Overcoming or Ignoring the Effects of Fear, Intimidation, or Panic"],
        "Inabilities": [],
        "Features": {},
        "Additional Equipment": {},
        "Link to Starting Adventure": [
            "By staying calm in a difficult situation, you gained the trust of the other PCs.",
            "No one else would take up the task, but you weren’t afraid to try.",
            "You were investigating a series of strange occurrences, which led you to the other PCs and your current "
            "situation.",
            "Sometimes you need to blow off a little steam and helping the other PCs seemed like a way to do that.",
        ],
    },
    "Vicious": {
        "Stat Bonuses": [0, 0, 0],
        "Skills": ["Tracking"],
        "Inabilities": [],
        "Features": {
            "Skill":
                "You are trained in tracking creatures. If a creature has wronged you, the tracking task is eased.",
            "Bloodthirsty":
                "Once you begin fighting, you see only red. You inflict 2 additional points of damage with any attack.",
            "Berserk":
                "Once you begin fighting, it’s hard for you to stop. In fact, it’s a difficulty 2 Intellect task to "
                "do so, even if your foe surrenders or you’ve run out of foes. If the latter occurs and you fail to "
                "stop, you attack the nearest ally within short range.",
        },
        "Additional Equipment": {"Equipment": ["A List of Those Who Have Wronged You"]},
        "Link to Starting Adventure": [
            "Another PC saw you take down a mean drunk in a tavern, not realizing you were the one who started the "
            "fight.",
            "You wanted to get away from a bad situation, so you went with the other PCs.",
            "You want to change, and you hope that being with the other PCs will help you calm yourself.",
            "One of the other PCs asked you to come along, believing that your viciousness could be harnessed for the "
            "benefit of the mission.",
        ],
    }
}

descriptors = dict(discovery_descriptors, **destiny_descriptors)

focus_template = {
    "Description": "",
    "Connection": [],
    "Additional Equipment": {},
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

discovery_foci = {
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
        "Additional Equipment": {
            "Artifacts": ["a device that sprays inanimate objects to make them fire-resistant"]
        },
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
        "Additional Equipment": {
            "Artifacts": ["A crystal or jewel artifact that, when worn against your forehead or temple, adds 1 point "
                          "to your Intellect Pool. If you’re ever without the artifact, subtract 5 points "
                          "from your Intellect Pool; the points are restored if you regain the item."]
        },
        "Core Features": {"Mental Esoteries": "When you apply Effort to the special abilities that control minds, like "
                                              "the Mind Control esotery, the Mind Reading esotery, or the Crowd Control "
                                              "trick of the trade, you get a free level of Effort on that task. "
                                              "Enabler."},
        "Major Effect Suggestions": "You can take another action on that same turn.",
        "Minor Effect Suggestions": "The range or duration of the mental power is doubled.",
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
        "Additional Equipment": {
            "Equipment": ["3 days of food for your Animal Companion", "Leash, Collar, or equivalent"]
        },
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
                      "it provides an asset to your attacks). Enabler.", },
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
        "Additional Equipment": {
            "Oddities": ["a pen-sized oddity that tells the weight of whatever you point it at (within short range). "
                         "The weight is displayed on a small glass plate in runes that only you can decipher."]
        },
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
        "Additional Equipment": {
            "Oddities": ["An oddity that appears to be a piece of clear glass in a synth frame. By manipulating"
                         " hidden switches on the frame, you can make random moving images appear on the glass. "
                         "The images are usually strange and sometimes incomprehensible."]
        },
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {},
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
        "Additional Equipment": {"Equipment": ["A Musical Instrument or other tools to perform"]},
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
        "Additional Equipment": {},
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
        "Additional Equipment": {"Equipment": ["Explorer's pack"]},
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
        "Additional Equipment": {"Equipment": ["Extremely Stylish Clothes", "A Jeweled Weapon"]},
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
        "Additional Equipment": {},
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
            '3': {"CHOICE": {
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
        "Additional Equipment": {"Equipment": ["A bag of light tools", "A variety of parts to repair yourself"]},
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
            '3': {"CHOICE": {
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {"Artifacts": ["an accurate chronometer artifact that always lets you know when the "
                                               "next transformation is coming."]},
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {
            "Equipment":
                ["Boots that muffle your footsteps, giving you an asset on any roll made involving sneaky movement."],
        },
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
            '3': {"CHOICE": {
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {"Oddities": ["a directional compass."]},
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
        "Additional Equipment": {"Equipment": ["A Shield"]},
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
        "Additional Equipment": {"Equipment": ["a high-quality weapon of your choosing"]},
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
        "Additional Equipment": {
            "Equipment": ["a disguise kit", "three doses of a level 2 blade poison that inflicts 5 points of damage."],
        },
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
        "Additional Equipment": {},
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {
            "Equipment": ["a bag of miscellaneous batteries and power cells. Whenever you find a new device that "
                          "operates on batteries or cells (GM’s discretion), there is a 75 percent chance "
                          "that the bag contains one that will power the device if it depletes."]
        },
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {
            "Equipment": ["a book in which you keep notes of your favorite words, inspirational stories, and "
                          "speech anecdotes."],
        },
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {"Equipment": ["A bag of small tools."]},
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
            '3': {"CHOICE": {
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
            '6': {"CHOICE": {
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
        "Additional Equipment": {"Equipment": ["a bladed weapon made of stronglass that looks like ice"]},
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
            '3': {"CHOICE": {
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
        "Additional Equipment": {"Equipment": ["an additional book about the numenera."]},
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
            '3': {"CHOICE": {
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
        "Additional Equipment": {"Equipment": ["an additional light melee weapon."]},
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
            '3': {"CHOICE": {
                "Dual Medium Wield":
                    "You can use two light weapons or medium weapons at the same time (or one light weapon and one "
                    "medium weapon), making two separate attacks on your turn as a single action. This ability "
                    "otherwise works like the Dual Light Wield ability. Enabler.",
                "Precise Cut": "You inflict +1 damage with light weapons. Enabler."
            }},
            '4': {
                "Dual Defense": "When you wield two weapons, you are trained in Speed defense tasks. Enabler."
            },
            '5': {
                "Dual Distraction":
                    "(1+ Speed points) When you wield two weapons, your opponent’s next attack is hindered, and if "
                    "you apply Effort to your next attack against that same foe, you get a free level of Effort on "
                    "the task. Enabler."
            },
            '6': {"CHOICE": {
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
        "Additional Equipment": {"Equipment": ["a bag of light tools"]},
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
            '3': {"CHOICE": {
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
            '6': {"CHOICE": {
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
            '3': {"CHOICE": {
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
            '6': {"CHOICE": {
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
    },
}

destiny_foci = {
    "Absorbs Energy": {
        "Description": "Every movement is an expression of energy. You can harness this kinetic energy and transform "
                       "it into other kinds of energy. At first, once you absorb energy, you must use it before you "
                       "can absorb any more. You can use the absorbed energy as a weapon, or you can infuse an object "
                       "with dangerous energy that is released upon touch. Eventually, you will be able to use the "
                       "energy for nonviolent purposes, such as healing or invigorating creatures.",
        "Connection": [
            "Pick one other PC. For reasons unknown to you, this character is completely immune to the energy you "
            "release, whether you use it for help or harm.",
            "Pick one other PC. You knew of this character years ago, but you don’t think they knew you.",
            "Pick one other PC. You’re always trying to impress them, but you’re not even sure why.",
            "Pick one other PC. This character has a habit that annoys you, but you’re otherwise quite impressed with "
            "their abilities.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "The energy you release is even more potent than you thought. Your opponent loses "
                                    "their next action.",
        "Minor Effect Suggestions": "The energy you release is even more potent than you thought. Your opponent’s "
                                    "actions are hindered next round.",
        "Tiers": {
            '1': {
                "Absorb Kinetic Energy":
                    "You absorb a portion of the energy of a physical attack or impact. You negate 1 point of damage "
                    "you would have suffered and store that point as energy. Once you have absorbed 1 point of "
                    "energy, you continue to negate 1 point of damage from any incoming blow or impact, "
                    "but the residual energy bleeds off with a flare of harmless light (you cannot store more than 1 "
                    "point at a time). Enabler.",
                "Release Energy":
                    "You release 1 point of energy you’ve absorbed—magnifying and focusing it into a blast of "
                    "energy—that strikes a single foe within long range for 4 points of damage. (If you don’t have "
                    "any kinetic energy absorbed, you can still use this ability, but it requires that you transform "
                    "a fraction of yourself into the blast, which costs 1 point of Might.) Action.",
            },
            '2': {
                "Energize Object":
                    "You infuse energy you have absorbed into an object, like a weapon. The object holds the energy "
                    "until it is touched by anyone but you, so putting it into your melee weapon or the ammo of a "
                    "ranged weapon allows the weapon to trigger the energy in combat. The energy inflicts 3 points of "
                    "damage on the creature touched in addition to any damage the weapon itself might do. You cannot "
                    "have more than one energized object on your person at a time. Action to initiate.",
            },
            '3': {"CHOICE": {
                "Absorb Pure Energy":
                    "You can also absorb and store energy from attacks made with pure energy (focused light, "
                    "radiation, transdimensional, psychic, etc.) or from conduits that direct energy, if you can make "
                    "direct contact. This ability does not change how many points of energy you can store. If you "
                    "also have Improved Absorb Kinetic Energy, you can absorb 2 points of damage from other energy "
                    "sources as well. Enabler.",
                "Improved Absorb Kinetic Energy":
                    "Instead of being able to absorb 1 point of damage from a physical attack or impact, "
                    "you can absorb 2 points. You can also store up to 2 points of energy from any source. However, "
                    "you can still only release energy 1 point at a time. Enabler.",
            }},
            '4': {
                "Overcharge Energy":
                    "When you use Release Energy, it inflicts an additional 2 points of damage. Enabler.",
            },
            '5': {
                "Energize Creature":
                    "(6+ Might points) You extend your Absorb Kinetic Energy ability to one creature within immediate "
                    "range so that they also can absorb energy from physical attacks and impacts for one hour. That "
                    "creature, however, cannot release excess energy as a blast. For each level of Effort you apply, "
                    "you can increase the number of targets you affect by one. If you have Absorb Pure Energy or "
                    "Improved Absorb Kinetic Energy, those abilities are also duplicated in your target when you use "
                    "Energize Creature. Action to initiate.",
            },
            '6': {"CHOICE": {
                "Energize Crowd":
                    "(9 Might points) You extend your Absorb Kinetic Energy ability to up to thirty creatures within "
                    "short range so that they also can absorb energy from physical attacks and impacts for one hour. "
                    "If you have Absorb Pure Energy or Improved Absorb Kinetic Energy, these creatures can use those "
                    "abilities as well. The creatures, however, cannot release excess energy as a blast. Action to "
                    "initiate.",
                "Overcharge Device":
                    "You infuse 1 point of energy you’ve stored into a device, such as an artifact or installation, "
                    "which raises its effective level on its next use by 3 (to a maximum of 10). Enabler.",
            }}
        },
    },
    "Acts Without Consequence": {
        "Description": "You’re a rebel. You resist the dictates of authority, you try to break away from the control "
                       "that society holds over you, and you like to flout traditions that you view as backward. "
                       "That’s not to say that you automatically disagree with anything or anyone you deal with. It’s "
                       "more that you believe certain institutions and conventions are foolish and even hurtful. This "
                       "is why you often press your luck and defy the status quo. Often enough, you get away with it. "
                       "\nIn fact, your success is more than a mere twist of statistics. You enjoy some kind of psychic"
                       " enhancement, implanted device, or attention of a datasphere spirit. You’ve also practiced "
                       "certain skills, behaviors, and attitudes that allow blame to slip off you like water off a "
                       "murden.",
        "Connection": [
            "Pick one other PC. Through a quirk of fate, this character is sometimes blamed for your exploits, even if "
            "they’re not near you.",
            "Pick one other PC. You recently discovered that they always seem to be able to track you when you Slip "
            "Into Shadow.",
            "Pick one other PC. You saved them from certain death by taking a lucky gamble. It could’ve gone either "
            "way, but in the end, they lived. If you’d lost, they would’ve certainly died.",
            "Pick one other PC. They rescued you from an awful predicament during one of the few times your luck "
            "failed you. You’re a bit embarrassed that they know you have limits.",
        ],
        "Additional Equipment": {
            "Equipment": ["a deck of cards"],
            "Oddities": ["A 'lucky' oddity of the DM's choice"]
        },
        "Core Features": {
            "Weird Ability":
                "You can choose to learn Danger Sense instead of one of the abilities granted by your type. \nDanger "
                "Sense (1 Speed point). Your initiative tasks are eased. You pay the cost each time the ability is "
                "used. Enabler.",
        },
        "Major Effect Suggestions": "A foe forgets about you unless you draw attention to yourself.",
        "Minor Effect Suggestions": "Your foe is surprised by or has a bad reaction to you for one round, during "
                                    "which time all its tasks are hindered.",
        "Tiers": {
            '1': {
                "Slip Into Shadow":
                    "(2+ Intellect points) You attempt to slip away from a selected target and hide from view in a "
                    "nearby shadow, behind a tree or a furnishing, or into the next room, even if in full view of the "
                    "target. For each level of Effort applied, you can attempt to affect one additional target, "
                    "as long as all your targets are next to each other. Action to initiate.",
                "Blameless":
                    "You are trained in one of the following: deception, stealth, or disguise. Enabler.",
            },
            '2': {
                "Get Away":
                    "(2 Speed points) After your action on your turn, you move up to a short distance or get behind "
                    "or beneath cover within immediate range. Enabler.",
            },
            '3': {"CHOICE": {
                "Goad":
                    "(2 Might points) After you successfully attack a creature, Speed defense tasks by all others "
                    "against the creature’s attacks are eased until the end of the next round. Enabler.",
                "Seize Opportunity":
                    "(4 Speed points) If you succeed on a Speed defense roll to resist an attack, you gain an action. "
                    "You can use it immediately even if you have already taken a turn in the round. You can use this "
                    "ability once per round, after which you don’t take an action during the next round. If you use "
                    "this action to attack, the attack is eased. Enabler.",
            }},
            '4': {
                "Uncanny Luck":
                    "(4 Speed points) When you roll for a task and succeed, roll again. If the second number rolled "
                    "is higher than the first, you get a minor effect. If you roll the same number again, "
                    "you get a major effect. If you have Uncanny Luck from another source or a similar ability, "
                    "it’s your choice (no roll required) whether you get a minor effect, a major effect, "
                    "or a free activation of one of your tier 1–3 focus abilities. Enabler.",
            },
            '5': {
                "Invisibility":
                    "(4 Intellect points) You become invisible for ten minutes. While invisible, you are specialized "
                    "in stealth and Speed defense tasks. This effect ends if you do something to reveal your presence "
                    "or position—attacking, using an ability, moving a large object, and so on. If this occurs, "
                    "you can regain the remaining invisibility effect by taking an action to hide your position. If "
                    "you have a type ability that also confers invisibility, using either ability allows you to "
                    "remain invisible for twice as long as the duration specified. Action to initiate or reinitiate.",
            },
            '6': {"CHOICE": {
                "No Fate":
                    "You don’t believe in any luck except that which you make for yourself. If you fail on a task "
                    "(including an attack or a defense), you can change the die result to a natural 20. (That still "
                    "might not be enough to succeed if the difficulty is higher than 6.) Once you use this ability, "
                    "it is not available again until after you make a ten-hour recovery roll. This ability doesn’t "
                    "work if you roll a natural 1 for an attempted task, unless you also have Twist of Fate or a "
                    "similar ability. Enabler.",
                "Twist of Fate":
                    "When you roll a 1, you can reroll. You must use the new result, even if it’s another 1. Enabler.",
            }}
        },
    },
    "Adjures the Leviathan": {
        "Description": "You have the power to command the Leviathan—your name for the horrific things that wait in "
                       "the empty ruins or hunt in the dark beyond the town walls, creatures with long teeth, "
                       "hellish fury, and a hunger for human flesh. The Leviathan is the spirit of the predatory, "
                       "the monstrous, and the sociopathic. Sometimes, you suspect the term applies to a specific "
                       "variety of creature, all descended from a literal entity called the Leviathan—a bloodline you "
                       "perhaps share in some small way, explaining why you can command and control these terrible "
                       "creatures that preferentially hunt humans over all other flesh.",
        "Connection": [
            "Pick one other PC. A creature you control will take commands both from this character and from you. But "
            "if it ever receives conflicting commands, it turns on you both.",
            "Pick one other PC. You captured a creature for this character, but it promptly tried to kill them. "
            "They still have scars from the incident.",
            "Pick one other PC. You are pretty sure you can command that PC as a creature if you apply enough Effort "
            "(though you don’t think you can capture the PC). You haven’t tried, and you’re not sure you should; it "
            "might unlock some previously bestial part hidden inside them.",
            "Pick one other PC. You saved them from a creature attack, and they owe you their life.",
        ],
        "Additional Equipment": {"Equipment": ["a leash"]},
        "Core Features": {},
        "Major Effect Suggestions": "A creature you control takes an immediate extra action of your choice.",
        "Minor Effect Suggestions": "One additional creature takes no action for a round.",
        "Tiers": {
            '1': {
                "Adjure Creature":
                    "(2+ Intellect points) For one minute, you can verbally control a living, nonhumanoid creature of "
                    "up to level 2 within short range whose motive is some variant of “hungers for flesh,” commanding "
                    "it to do simple tasks on your behalf. \nAlternatively, you can force up to three such creatures "
                    "within range to take no actions for as long as you focus all your attention on them. Every "
                    "round, each member of the group can attempt to escape your control. Whichever effect you "
                    "attempt, you can apply Effort to increase the maximum level of the affected creature. Thus, "
                    "to command a level 4 creature to do simple tasks on your behalf (two levels above the normal "
                    "limit), you must apply two levels of Effort. Action to initiate.",
                "Ninth World Bestiary Knowledge":
                    "You are trained in the lore of flesh-eating, non- humanoid creatures—recognizing them,  "
                    "knowing their weaknesses, and knowing their habits and behaviors. Enabler.",
            },
            '2': {
                "Capture Creature":
                    "Instead of attempting to use your Adjure Creature on a target, you can attempt to capture it, "
                    "as long as it is level 1 or level 2. A captured creature becomes tame in your presence, "
                    "becoming a follower. As a special exception to the rules for followers, one of your captured "
                    "creature’s modifications is for attacks, and the other modification must be for something basic "
                    "that a non-intelligent creature could help you with, such as perception or initiative. You can "
                    "have only one captured creature at a time. Enabler.",
            },
            '3': {"CHOICE": {
                "Enrage Creature":
                    "(3+ Intellect points) With a touch and whispered word, you can trigger a biological response in "
                    "a creature you’ve captured with Capture Creature, causing it to fly into a bone-ripping rage for "
                    "up to one minute. During this period, treat the creature as a level 5 creature that inflicts 6 "
                    "points of damage each round. However, after this extreme effort, the creature either dies or "
                    "becomes so enfeebled by its expenditure of energy that it becomes ineffective for several days. "
                    "Each level of Effort you apply increases the temporary level of the creature (to a maximum of "
                    "level 10) and damage done by 1. Action to initiate.",
                "Vigor of the Leviathan": "You can make an extra one-action recovery roll each day. Enabler.",
            }},
            '4': {
                "Duo":
                    "You can use your tier 2 ability to have two Captured Creatures at a time instead of just one, "
                    "and you can capture creatures of up to level 3. Enabler.",
            },
            '5': {
                "Lash of the Tamer":
                    "(4+ Intellect points) You can demand more of the creatures that you have captured. One creature "
                    "you have captured within short range is granted an additional, immediate action, which they can "
                    "take out of turn. Alternatively, you can attempt to provide any creature within short range an "
                    "additional, immediate action, which they can take out of turn, but to do so, you must apply a "
                    "level of Effort. Action. "
            },
            '6': {"CHOICE": {
                "Become the Leviathan":
                    "(9+ Intellect points) You change shape into a monstrous creature up to three times your normal "
                    "size for one minute. When you do, you become practiced in using whatever natural weapons—teeth, "
                    "claws, tail, and so on— your new shape possesses. You also add 15 temporary points to your Might "
                    "Pool and +3 to Might Edge, and you deal 4 additional points of damage with melee attacks. For "
                    "each level of Effort you apply, your size increases by 5 feet (1.5 m) and you add 1 additional "
                    "temporary point to your Might Pool. Becoming the Leviathan is incredibly taxing. While doing so, "
                    "your Speed defense tasks are hindered by two steps. After you revert to normal size, "
                    "you are exhausted, you descend one step on the damage track, and you can’t  use this ability "
                    "again until after your next ten- hour recovery roll. Action to change. Action to  revert or take "
                    "some other shape.",
                "Menagerie":
                    "You can use your tier 2 ability to have up to four Captured Creatures at one time instead of "
                    "just two. Enabler.",
            }}
        },
    },
    "Augments Flesh with Grafts": {
        "Description": "Machines can be upgraded and improved, and the human body is just an organic machine. Your "
                       "goal is to keep improving your physical form, replacing obsolete parts of your body with new "
                       "grafts and trying to become supremely efficient at your normal and augmented biological "
                       "processes. Whether you do this with technology or pieces from other creatures depends on what "
                       "you find in your explorations and your estimation of your flaws and shortcomings. You don’t "
                       "believe it’s possible to achieve perfection—perfection is an ongoing process, not a final "
                       "state. If following this path makes you something more than human, so be it. You left behind "
                       "childish toys and forms to become an adult, so you are willing to leave your humanity behind "
                       "in order to become something greater.",
        "Connection": [
            "Pick one other PC. They have an ability you’d like as a graft, and you want to find a creature or cypher "
            "that duplicates that ability.",
            "Pick one other PC. They once saved your life when one of your surgeries had a complication.",
            "Pick one other PC. You think they’re offended or disgusted by your grafts, and you want to demonstrate "
            "the value of your abilities.",
            "Pick one other PC. They’re interested in grafts, but you’ve rebuffed their requests because you think "
            "they’d have a fatal reaction to the surgery.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "Your foe is especially vulnerable to some aspect of one of your implants, "
                                    "like an allergy or radiation sensitivity. Make an immediate attack against that "
                                    "foe (using the same stat as the action that caused the major effect). If the "
                                    "attack succeeds, it deals 3 points of damage (ignores Armor).",
        "Minor Effect Suggestions": "An upgraded body part is especially effective or efficient at a particular "
                                    "physical task. You gain an asset to similar actions involving the same task ("
                                    "such as making attacks against the same foe or dealing with a physical "
                                    "obstacle).",
        "Tiers": {
            '1': {
                "Autodoctor":
                    "You are trained in healing, performing surgical procedures, and withstanding pain. You can "
                    "perform surgeries on yourself, remaining conscious while you do so. Enabler.",
                "Surgical Graft":
                    "You use your knowledge to surgically attach a cypher to your body, linking it to your nerves and "
                    "muscles. Activating or using this cypher is as natural for you as breathing and doesn’t require "
                    "any obvious motion (allowing you to activate it secretly). A grafted cypher still counts toward "
                    "your cypher limit, but it is not destroyed after one use. A grafted cypher has a depletion of 1 "
                    "in 1d10. The GM may allow you to graft biological parts from other creatures, giving you an "
                    "ability like one of the creature’s abilities. This is treated exactly the same as if it were a "
                    "grafted cypher (that is, it counts toward your cypher limit, has a depletion of 1 in 1d10, "
                    "etc.), except for the graft to work you must make a surgery skill roll against a difficulty "
                    "chosen by the GM. The less human the creature is, the more difficult it is to perform a "
                    "successful grafting surgery. Action to initiate surgery, one hour to complete.",
            },
            '2': {
                "Augment Graft":
                    "(2+ Intellect points) When you activate a grafted cypher, add 1 to its level. Every level of "
                    "Effort applied increases the level of the grafted cypher by 1. You can’t increase the grafted "
                    "cypher’s level above 10. If you have the Jack trick of the trade Augment Cypher, when you apply "
                    "Effort to augment a graft, you get a free level of Effort on that task. Enabler.",
            },
            '3': {"CHOICE": {
                "Hardy":
                    "You gain +5 to your Might Pool. These additional points can be used only to absorb damage. You "
                    "can’t spend them to apply Effort to rolls. Enabler.",
                "Recharge Graft":
                    "(2+ Intellect points) You recharge a grafted cypher that was depleted in the past ten minutes, "
                    "allowing it to be used again. You must touch the graft, spend 1 XP, and succeed at a surgery "
                    "roll (difficulty equal to the level of the graft) to recharge it; otherwise the graft remains "
                    "spent and useless. Some grafts (particularly pills and injections) cannot be recharged in this "
                    "way. In addition to the normal options for using Effort, you can also choose to use Effort to "
                    "recharge a graft that was depleted more than ten minutes ago, with each level of Effort "
                    "extending this time period by ten minutes. If you have the Jack trick of the trade Recharge "
                    "Cypher, the time increments for recharging a graft are one hour each instead of ten minutes "
                    "each. Action.",
            }},
            '4': {
                "Artifact Fusion":
                    "You can surgically graft artifacts to your body. These fused devices function as if they were "
                    "one level higher. Enabler.",
                "Additional Cypher":
                    "The number of cyphers you can bear (whether or not they are grafts) increases by one. Enabler.",
            },
            '5': {
                "Faster Grafting":
                    "You’ve permanently altered your body to make it faster and easier to add or remove grafts. "
                    "You gain an asset on surgical tasks, and adding or removing a graft takes only one minute "
                    "instead of an hour. Enabler.",
            },
            '6': {"CHOICE": {
                "Defensive Augmentation":
                    "By upgrading your nervous and immune systems, you are trained in Might defense and Speed defense "
                    "tasks. Enabler.",
                "Transhuman Organs":
                    "After a ten-hour surgical procedure where you upgrade or replace most of your internal organs "
                    "with new ones, you gain +5 to each of your three stat Pools. Enabler.",
            }}
        },
    },
    "Battles Automatons": {
        "Description": "Life is for the living—the biological. Automatons, animate machines, thinking machines, "
                       "and anything similar are abominations. You excel at battling these anathemas, cleansing the "
                       "world of their contaminating presence. \nMaybe your desire to battle automatons comes from "
                       "religious zealotry. Maybe it’s steeped in revenge for some past crime committed by a machine. "
                       "Maybe you don’t know why you’re driven to destroy animate machines. Maybe you’re just good at "
                       "it.",
        "Connection": [
            "Pick one other PC. You suspect that this character is put off by your hatred of animate machines. You "
            "can choose whether or not they know of your suspicions.",
            "Pick one other PC. You know that this character has suffered at the hands of automatons in the past, and "
            "perhaps you can convince them to help you in your calling. Regardless, you feel protective of them.",
            "Pick one other PC. This character does not appear to share your feelings about automatons. In fact, you "
            "believe that they might secretly have machine parts.",
            "Pick one other PC. This character comes from the same place you do, and you knew each other as children.",
        ],
        "Additional Equipment": {"Equipment": ["trophies torn off from automatons"]},
        "Core Features": {
            "Anti-Machine Abilities":
                "You are trained in understanding numenera. In addition, if your type grants you special abilities "
                "that inflict damage, they inflict 1 additional point of damage to automatons and similar beings, "
                "and 1 fewer point of damage to biological, living targets. If you have abilities that normally would "
                "not work against automatons (like mind control), they will now. Enabler.",
        },
        "Major Effect Suggestions": "Your automaton foe experiences a major error and loses its next turn.",
        "Minor Effect Suggestions": "Your automaton foe experiences an error for one round, during which time all "
                                    "tasks it attempts are hindered.",
        "Tiers": {
            '1': {
                "Machine Vulnerabilities":
                    "You inflict 3 additional points of damage against automatons and animate machines of all kinds. "
                    "Enabler.",
            },
            '2': {
                "Defense Against Automatons":
                    "You have studied your enemy and are trained in anticipating the actions that an automaton or "
                    "machine is likely to take in a fight. Defense tasks you attempt against these foes are eased. "
                    "Enabler.",
                "Machine Hunting":
                    "You are trained in tasks associated with tracking, spotting, or otherwise finding automatons and "
                    "animate machines. You are also trained in all stealth tasks. Enabler.",
            },
            '3': {"CHOICE": {
                "Disable Mechanisms":
                    "(3 Speed points) With a keen eye and quick moves, you disrupt some of an automaton’s functions "
                    "and inflict upon it one of the following maladies: \n* The difficulty of all its tasks is "
                    "hindered for one minute. \n* The automaton’s speed is halved. \n* The automaton can take no "
                    "action for one round. \n* The automaton deals 2 fewer points of damage (minimum 1 point) for one "
                    "minute. \n You must touch the automaton to disrupt it (if you are making an attack, it inflicts "
                    "no damage). Action.",
                "Surprise Attack":
                    "If attacking from a hidden vantage, with surprise, or before your opponent has acted, you get a "
                    "free level of Effort on the attack. On a successful hit, you inflict 2 additional points of "
                    "damage. Enabler.",
            }},
            '4': {
                "Automaton Fighter":
                    "When fighting an automaton or intelligent machine, you are trained in attacks and defense. "
                    "Enabler.",
                "Pierce Metal Hides": "You ignore 2 points of Armor on an automaton. Enabler.",
            },
            '5': {
                "Drain Power":
                    "(5 Speed points) You affect the main power source of the automaton, inflicting upon it all four "
                    "conditions listed for Disable Mechanisms at once. You must touch the automaton to do this (if "
                    "you are making an attack, it inflicts no damage). Action.",
            },
            '6': {"CHOICE": {
                "Blind Machine":
                    "(6 Speed points) You deactivate the sensory apparatus of the machine, making it effectively "
                    "blind until it can be repaired. You must either touch the target or strike it with a ranged "
                    "attack (inflicting no damage). Action.",
                "Deactivate Mechanisms":
                    "(5+ Speed points) You make a melee attack that inflicts no damage against a machine. Instead, "
                    "if the attack hits, make a second Speed-based roll. If successful, a machine of level 3 or lower "
                    "is deactivated for one minute. For each additional level of Effort applied, you can affect one "
                    "higher level of machine or you can extend the duration for an additional minute. If you have the "
                    "Wright special abilities Scramble Machine or Disable Machine (or a type ability that works "
                    "similarly), when you apply a level of Effort to any of them, you gain an additional free level "
                    "of Effort. Action.",
            }}
        },
    },
    "Brandishes an Exotic Shield": {
        "Description": "Anyone can use a shield. But few can project a protective force field that crackles with "
                       "otherworldly energy. Maybe your ability comes from a childhood encounter with a strange "
                       "machine or a metallic nodule that protrudes above your flesh along your spine, or perhaps it "
                       "is something that people in your family are capable of once every few generations. You use "
                       "your force field to not only protect yourself, but to aggressively bash those who would do "
                       "you harm. At first, you can create only a small protective plane. But as your skills improve, "
                       "you can learn to throw it at foes and have it rebound, heal allies, and release an explosion "
                       "of destructive energy each time it strikes home.",
        "Connection": [
            "Pick one other PC. You overheard them say that anyone who uses a shield doesn’t really know how to fight. "
            "You’re looking for an opportunity to prove them wrong.",
            "Pick one other PC. Someone related to this character gave you the plans to create, or themselves created, "
            "your shield.",
            "Pick one other PC. You rescued them from a bad situation.",
            "Pick one other PC. You’re drawn to them and don’t know why. There’s just something about them. A shared "
            "destiny? Or destined to become bitter foes one day?",
        ],
        "Additional Equipment": {},
        "Core Features": {
            "Shield Abilities":
                "If you wish, you can replace one of your tier 1 type abilities with Force Fall. "
                "\nForce Fall: (1 Speed point) If you fall, you can use your force field shield to absorb the impact "
                "of landing and gain +5 Armor against damage you would otherwise take from the fall. Enabler.",
        },
        "Major Effect Suggestions": "Your bash your target, and they are dazed for one minute, during which time their "
                                    "tasks are hindered.",
        "Minor Effect Suggestions": "You bash your target and knock them prone.",
        "Tiers": {
            '1': {
                "Force Field Shield":
                    "You manifest a small plane of pure force, which takes on a shield-like shape with the barest "
                    "flicker of a thought. You can dismiss it just as easily. To use the force shield, you must hold "
                    "it in one of your hands. You are practiced in using your exotic shield in one hand as a light "
                    "melee weapon; however, if you attack with both your shield and a weapon held in the other hand, "
                    "both attacks are hindered. When you are unconscious or sleeping, the force field dissipates. "
                    "Enabler.",
                "Force Bash":
                    "(1 Might point) This is a pummeling melee attack you make with your force shield. Your attack "
                    "inflicts 1 fewer point of damage than normal but dazes your target for one round, during which "
                    "time all tasks it performs are hindered. Enabler.",
            },
            '2': {
                "Enveloping Shield":
                    "Your force shield produces an envelope of force that enfolds you while you are holding the "
                    "shield, granting you +1 to Armor. Enabler.",
            },
            '3': {"CHOICE": {
                "Healing Pulse":
                    "(3 Intellect points) You and all targets you choose within immediate range gain the immediate "
                    "benefits of using one of their recovery rolls (as long as it is not their ten-hour recovery "
                    "roll) without having to spend an action, ten minutes, or one hour. Targets regain points to "
                    "their Pools immediately but mark off that recovery use. PCs who have already used up their "
                    "one-action, ten-minute, and one-hour recovery rolls for the day gain no benefit from this "
                    "ability. NPCs targeted by this ability regain a number of health points equal to their level. "
                    "Action.",
                "Throw Force Shield":
                    "You can throw your force shield up to short range as a light ranged weapon. Whether the shield "
                    "hits or misses, it immediately dissipates and then reforms in your grasp. Enabler.",
            }},
            '4': {
                "Energized Shield":
                    "Your force shield now pulses with dangerous energy whenever you manifest it. Each time you use "
                    "your shield as a melee or ranged weapon, it inflicts +3 damage. Enabler.",
            },
            '5': {
                "Force Wall":
                    "(5 Intellect points) You can trigger the energy in your force shield to expand outward in all "
                    "directions to create an immobile plane of solid force up to 20 feet by 20 feet (6 m by 6 m) for "
                    "up to one hour or until you take your shield back. (The force shield becomes the force wall.) "
                    "The plane of the force wall conforms to the space available. While the force wall remains in "
                    "place, the only other focus ability you can use is Healing Pulse. Action to initiate.",
            },
            '6': {"CHOICE": {
                "Bouncing Shield":
                    "If you throw your force shield as a light weapon at a target within short range, whether it hits "
                    "or misses, it will attack up to two additional targets within short range. Effort or other "
                    "modifiers applied to the first attack affect all other targets as well. Whether you hit all, "
                    "some, or none of your targets, the shield dissipates and then reforms in your grasp. (If you "
                    "choose Bouncing Shield and have previously taken the tier 3 ability Throw Force Shield, "
                    "you have the option to exchange your tier 3 ability for Healing Pulse.) Enabler.",
                "Shield Burst":
                    "When you make a melee or ranged attack and hit with the force shield, it releases an explosion "
                    "of energy, inflicting an additional 2 points of damage on the target and everything within "
                    "immediate range of the target. If you applied Effort to inflict additional damage as part of the "
                    "attack, each level of Effort inflicts only 2 additional points to all targets instead of 3 "
                    "points. If you use Shield Burst with a melee attack, you and creatures behind you are not "
                    "affected by this explosion. If you use Shield Burst as a ranged attack, the shield dissipates "
                    "after the attack and then reforms in your grasp. Enabler.",
            }}
        },
    },
    "Breaks Down Walls": {
        "Description": "Through some modification of your body—  mutation, mechanical enhancement, "
                       "nano- reinforcement, or something else—you have  the ability to smash through walls, "
                       "destroy weapons, shatter shackles, break devices, and otherwise annihilate objects that would "
                       "be difficult or even impossible for others to demolish. You’re a breaker. You do not flinch; "
                       "you punch right through that wall, smash that machine, and fold the enemy’s metallic sword in "
                       "half in an impressive and intimidating display. Depending on the method that gives you this "
                       "ability, your act might be accompanied by flashes of energy, sound, or acidic odors. Once you "
                       "display your impressive skills as a destroyer, your enemies sometimes surrender rather than "
                       "face an apparent force of nature like yourself.",
        "Connection": [
            "Pick one other PC. You accidentally struck this character once when you tried to break through a wall. "
            "It ruined your attempt and gave the character a nasty bruise that they claim still aches months later.",
            "Pick one other PC. You’re certain this character appreciates your abilities and is as impressed as you "
            "are with the sound of walls being smashed. This may or may not actually be the case.",
            "Pick one other PC. You and this character were childhood friends.",
            "Pick one other PC. This character provides excellent covering fire while you break down walls. If they "
            "use ranged attacks in the same round as you make a charge attack, they can fire their weapon through the "
            "hole you just made.",
        ],
        "Additional Equipment": {
            "Equipment":
                "A mechanism of some sort is fused with your flesh. You think it might have something to do with your "
                "ability to pierce solid material.",
        },
        "Core Features": {},
        "Major Effect Suggestions": "Your feat of destruction inspires you. You knock your opponent off their feet, "
                                    "and they lose their next action.",
        "Minor Effect Suggestions": "Your feat of destruction thrills you. You gain an asset to Speed defense tasks "
                                    "until your next action.",
        "Tiers": {
            '1': {
                "Breaker":
                    "You are trained in tasks related to damaging objects with the goal of breaking, piercing, "
                    "or demolishing them. (It is a Might action to damage an object, and on a success, the object "
                    "moves one step down the object damage track. If the Might roll exceeds the difficulty by two "
                    "steps, the object instead moves two steps down the object damage track. If the Might roll "
                    "exceeds the difficulty by four steps, the object moves three steps down the object damage track "
                    "and is immediately destroyed. Brittle material reduces the effective level of the object, "
                    "while hard material like wood or stone adds 1 to the effective level or 2 for very hard objects "
                    "like those made of metal.) Enabler.",
                "Hard as Synthsteel":
                    "To damage an object normally, the tool or weapon used to attack the object must be at least as "
                    "hard as the object itself. However, your hands and body automatically adjust so that, "
                    "for the purpose of breaking things, they momentarily become at least as hard as the object you "
                    "are attempting to damage or break. This ability doesn’t apply if you’re attempting to break "
                    "through force fields, unless you have the tier 4 ability Force to Reckon With. Enabler.",
            },
            '2': {
                "Field of Destruction":
                    "(4 Might points) When you cause an object to descend one or more steps on the object damage "
                    "track, you gain 1 additional point of Armor for one minute. Enabler.",
            },
            '3': {"CHOICE": {
                "Break Through":
                    "(4 Might points) You can move up to a short distance and attempt to break through a section of "
                    "wall at some point along the way, with a difficulty equal to the wall’s level. Your attempt is "
                    "hindered by one step for every 6 inches (15 cm) thickness of the wall. You can’t break through "
                    "force fields using this ability, unless you have the tier 4 ability Force to Reckon With. On a "
                    "failed attempt, you take 4 points of damage. Even if you successfully break through, "
                    "you still take 1 point of damage. This leaves a hole the size of your body in the barrier, "
                    "which others can use to pass through it. If you have a special ability from your type that allows "
                    "you to move and take an action, when you use this ability, you gain an asset to break through the "
                    "wall. Action.",
                "Machine Vulnerabilities":
                    "You inflict 3 additional points of damage against automatons and animate machines of all kinds. "
                    "Enabler.",
            }},
            '4': {
                "Force to Reckon With":
                    "You can break through force fields and energy barriers as if they were physical walls. Enabler.",
            },
            '5': {
                "Jump Attack":
                    "(5 Might points) You attempt a difficulty 4 Might task to jump high into the air as part of your "
                    "melee attack action. If you succeed at the jump and your attack hits, you inflict 3 additional "
                    "points of damage and knock the foe prone. If you fail at the jump, you still make your normal "
                    "attack roll, but you don’t inflict the extra damage or knock down the opponent on a hit. In "
                    "addition to the normal options for using Effort, you can also choose to use Effort to enhance "
                    "your jump; each level of Effort used in this way adds +2 feet (60 cm) to the height and +1 "
                    "damage to the attack. If you have the Glaive special ability of the same name, when you use "
                    "either, the Might task to jump high as part of the attack is difficulty 2 instead of 4. Action.",
            },
            '6': {"CHOICE": {
                "Break the Ranks":
                    "(6 Speed points) You move up to a short distance and attack up to four different foes as a "
                    "single action as long as they are all along your path. Any modifiers that apply to one attack "
                    "apply to all the attacks you make. If you have a special ability from your type that allows you "
                    "to move and take an action, when you use Break the Ranks, you gain an asset to attacking these "
                    "foes. Action.",
                "Destroyer":
                    "(6 Might points) If you succeed on a Might task to damage an object, instead of descending one "
                    "step on the damage track, the object descends all three steps and is destroyed. Action.",
            }}
        },
    },
    "Builds Tomorrow": {
        "Description": "One of your favorite pastimes involves imagining what the skylines of the previous worlds "
                       "might have looked like. Their inspiring heights, strange shapes, colors that human eyes can’t "
                       "see, connections between structures that allowed the unknowable peoples of those bygone eras "
                       "to step from one to the next . . . Well, you don’t know for certain what it must have been "
                       "like, but you gain just as much pleasure imagining the future you will build, using the seeds "
                       "of ancient knowledge as your guide for tomorrow.",
        "Connection": [
            "Pick one other PC. This character seems able to use all the objects and structures you craft with ease, "
            "even when you hide how to access certain functions.",
            "Pick one other PC. This character knows a few things that can help when the objects or structures you "
            "crafted need repair.",
            "Pick one other PC. This character has a special tool that you think would be perfect for your own set, "
            "but they regard it as a keepsake or are otherwise reluctant to give it up, even though they don’t seem "
            "to know what it’s good for.",
            "Pick one other PC. When you were developing a plan from a seed of knowledge from the prior worlds, this "
            "character was burned in an unexpected incident. They still have a small scar.",
        ],
        "Additional Equipment": {
            "Equipment": ["A Numenera Plan for a Cypher or Installation", "a bag of light tools"],
            "Iotum": {"Io": 3, "Responsive Synth": 3},
            "Parts": 3,
        },
        "Core Features": {},
        "Major Effect Suggestions": "The object or structure creates some startling effect that causes the foe to lose "
                                    "their next turn.",
        "Minor Effect Suggestions": "You are elated with how well an object you crafted is functioning, easing Speed "
                                    "defense tasks for the next round.",
        "Tiers": {
            '1': {
                "Natural Crafter": "You are trained in crafting numenera. Enabler.",
                "Seeds of a Plan":
                    "You immediately gain two new plans to create any object of up to level 3 plus your tier. Each "
                    "time you advance a tier, you can gain two additional plans of up to level 3 plus your tier. "
                    "Enabler.",
                "Starting Iotum":
                    "You have, find, or otherwise obtain a cache of iotum sufficient to build one installation or "
                    "cypher that you have a plan for. Enabler.",
            },
            '2': {
                "Customize Creation":
                    "(2 XP) When you craft an installation, you can modify it to possess one additional ability from "
                    "the Builds Tomorrow Customization Table. You can modify only installations. Customization occurs "
                    "as part of the time it would normally take you to complete the crafting project. Enabler.",
            },
            '3': {"CHOICE": {
                "Disable Machine":
                    "(3+ Intellect points) With a few deft touches, you infuse a powered device of level 3 or lower "
                    "with conflicting instructions. The device is destroyed or disabled for at least one minute, "
                    "depending on its size and complexity. The GM may rule that the disabling effect lasts until the "
                    "device is repaired. For each additional level of Effort applied, you can increase the maximum "
                    "level of the target by one. Thus, to overload a level 5 device (two levels above the normal "
                    "limit), you must apply two levels of Effort. If you have the Wright ability of the same name, "
                    "when you apply a level of Effort on either ability, you get a free level of Effort. Action.",
                "Improvised Repair":
                    "(5 Intellect points) When an object or structure with a depletion chance becomes depleted, "
                    "you can temporarily repair it with just a few rounds of tinkering. This grants an artifact a new "
                    "depletion chance of 1d6 or an installation (which typically has a long-term depletion chance of "
                    "days, weeks, or months of use per check) an additional 1d6 days of operation. Once an object or "
                    "structure has benefited from Improvised Repair once, it can’t be repaired again with this "
                    "ability. Instead, it must undergo actual repair. Action to initiate, a few rounds to complete.",
            }},
            '4': {
                "Fast Builder":
                    "When you attempt a crafting task, you lower the assessed difficulty for creating a complex "
                    "object or structure by 1. Enabler.",
            },
            '5': {
                "Dual Customization":
                    "(2 XP) When you use Customize Creation, you can modify the object or structure to possess a "
                    "second additional ability from the Builds Tomorrow Customization Table for an additional 2 XP. "
                    "You can modify artifacts, installations, vehicles, and automatons with this ability, "
                    "but never cyphers. Additional customization of a creation occurs as part of the time it would "
                    "normally take you to complete the crafting project. Enabler.",
            },
            '6': {"CHOICE": {
                "Deluxe Custom Options":
                    "(2 XP) When you craft a numenera object or structure, you can modify it to possess one "
                    "additional ability from the Builds Tomorrow Customization Table as normal, or to possess one "
                    "additional ability from the Deluxe Custom Options Table. You can modify artifacts, "
                    "installations, vehicles, and automatons with this ability, but never cyphers. Customizing a "
                    "creation occurs as part of the time it would normally take you to complete the crafting project. "
                    "Enabler.",
                "Triple Customization":
                    "(2 XP) When you use Customize Creation and Dual Customization, you can modify the object or "
                    "structure to possess a third additional ability from the Builds Tomorrow Customization Table for "
                    "an additional 2 XP. You can modify artifacts, installations, vehicles, and automatons with this "
                    "ability, but never cyphers. Additional customization of a creation occurs as part of the time it "
                    "would normally take you to complete the crafting project. Enabler.",
            }}
        },
    },
    "Dances with Dark Matter": {
        "Description": "You’ve felt the edges of something more real than the substanceless shadows that dance behind "
                       "the light—something you dubbed dark matter. It responded to you, almost like a living thing. "
                       "When you made shadow puppets, they were dark matter condensed and became briefly real. As you "
                       "grew older, you learned to harness your gift for more than play. You can condense dark matter "
                       "from thin air, pulling it from the void spaces or a transdimensional pocket that few others "
                       "can access. You don’t fear dark matter, but others should when you’re around.",
        "Connection": [
            "Pick one other PC. This character also likes the dark. You both gain +1 on any die rolls when you "
            "collaborate on the same task, fight the same foe, and so on.",
            "Pick two other PCs. You think you once saw them doing something illegal at night. You can choose whether "
            "or not to share that information. The characters can choose whether it was really them (it could have "
            "been neither, one, or both), and they may or may not share that information in return.",
            "Pick one other PC. This person always seems to see you, even when you’re totally cloaked by darkness.",
            "Pick one other PC. This character once flashed a cypher in your eyes so brightly that you were blinded "
            "for several days. You recovered, but you keep an eye on this character, just in case.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "Darkness thickens and momentarily clogs your foe’s throat like a wad of felt. "
                                    "Coughing and choking, they lose their next turn.",
        "Minor Effect Suggestions": "Darkness is drawn to your foe’s eyes, hindering any attacks the foe attempts on "
                                    "its next turn.",
        "Tiers": {
            '1': {
                "Ribbons of Dark Matter":
                    "(2 Intellect points) For the next minute, dark matter condenses within an area within long range "
                    "that is no bigger than an immediate distance in diameter, manifesting as swirling ribbons. All "
                    "tasks attempted by creatures in the area are hindered, and leaving the area requires the "
                    "creature’s entire action to move. You can dismiss the dark matter early as an action. Action to "
                    "initiate.",
            },
            '2': {
                "Void Wings":
                    "(3 Intellect points) Swirling ribbons of weird matter grasp you and lift you up, allowing you to "
                    "fly for one round as quickly as you can move. Enabler.",
            },
            '3': {"CHOICE": {
                "Dark Matter Shroud":
                    "(4 Intellect points) Ribbons of dark matter condense and swirl about you for up to one minute. "
                    "This shroud eases your Speed defense tasks, inflicts 2 points of damage to anyone who tries to "
                    "touch you or strike you with a melee attack, and gives you +1 Armor. Action to initiate.",
                "Dark Matter Strike":
                    "(4 Intellect points) When you attack a foe within long range, dark matter condenses around your "
                    "target and entangles its limbs, holding it in place and easing your attack by two steps. The "
                    "ability works for whatever kind of attack you use (melee, ranged, energy, and so on). Enabler.",
            }},
            '4': {
                "Dark Matter Shell":
                    "(5 Intellect points) For the next minute, you cover yourself with a shell of dark matter. Your "
                    "appearance becomes a dark silhouette, and you gain an asset to sneaking tasks and gain +1 to "
                    "your Armor. The dark matter shell works seamlessly with your desires, and if you apply a level "
                    "of Effort to any physical task while the shell persists, you can apply an additional free level "
                    "of Effort to that same task. Action to initiate.",
            },
            '5': {
                "Windwracked Traveler":
                    "(4+ Intellect points) You condense a wide wing of dark matter that can carry you through the air "
                    "for a period of up to one hour. For each level of Effort applied, you can add one hour to the "
                    "duration or carry one additional creature of your size or smaller. You must touch the additional "
                    "creatures for them to be tucked under your wing. They must remain relatively still while the "
                    "wing lasts or they will fall. In terms of overland movement, you fly at about 20 miles (32 km) "
                    "per hour and are not affected by terrain. Action to initiate.",
            },
            '6': {"CHOICE": {
                "Dark Matter Structure":
                    "(5 Intellect points) You can form dark matter into a large structure consisting of up to ten "
                    "10-foot (3 m) cubes. The structure can be somewhat complex, though everything has the same matte "
                    "black color from which no light shines. Otherwise, the structure can possess different "
                    "densities, textures, and capacities. This means it can include windows, doors with locks, "
                    "furnishings, and even decor, as long as it is all black as pitch. For example, you could shape "
                    "the dark matter into a large, defensible structure; a sturdy 100-foot (30 m) bridge; or anything "
                    "similar. The structure is a level 6 creation and lasts for 28 hours. You can’t keep more than "
                    "one such structure solid at any one time. Action.",
                "Embrace the Night":
                    "(7+ Intellect points) You fashion a truly horrifying facade of a creature from swirling ribbons "
                    "of dark matter and launch it at your foes within long range. You can attack each round against a "
                    "target within long range using the creation as your weapon. When you attack, the creature "
                    "inserts hair-fine tendrils of shadow into the target’s eyes and brain. The target takes 3 points "
                    "of Intellect damage (ignores Armor) and is stunned for one round so that it loses its next turn. "
                    "Alternatively, you can cause the creature to take other actions, as long as you are able to see "
                    "it and mentally control it as your action. The creature disperses after about a minute. Action "
                    "to initiate.",
            }}
        },
    },
    "Defends the Gate": {
        "Description": "You are a defender. Places are special to you, and seeing them overrun hurts your soul to its "
                       "core. Perhaps you had a bad experience once, where a place that you loved was lost in war. "
                       "After that, you vowed: never again. You sought out special training, and more than that, "
                       "a connection to the nanites that some possess but most people think of as magic. This "
                       "connection is conferred via mutation, a special device, psychic concentration, or some other "
                       "method that links you to the numenera. Your connection grows over time, granting you the "
                       "ability to defend a city, a wall, or even just a single but all-important gate.",
        "Connection": [
            "Pick one other PC. Though you once defended this character from a foe’s attack, you weren’t completely "
            "successful. This character still bears a scar (it’s up to them where and how prominent that scar is).",
            "Pick one other PC. You defended them once from an abhuman’s attack when they were debilitated. You were "
            "completely successful, saving this character’s life.",
            "Pick one other PC. You’re always trying to impress this character with your strength, ability to "
            "withstand pain, capacity for drink, and so on. Perhaps they are a rival, perhaps you desire their "
            "respect, or perhaps you’re romantically interested in them.",
            "Pick one other PC. This character seems to anticipate your next move almost before you begin it. When "
            "this character collaborates with you on the same task or defends the same area, both of you gain an "
            "asset to initiative tasks.",
        ],
        "Additional Equipment": {
            "Equipment": ["a strange device, either handheld or fused to your forearm"],
        },
        "Core Features": {},
        "Major Effect Suggestions": "Make an additional attack with your weapon on your turn.",
        "Minor Effect Suggestions": "The target is pushed back by your strong defense, so much so that it’s dazed for "
                                    "one round, during which time its tasks are hindered.",
        "Tiers": {
            '1': {
                "Fortified Position":
                    "(2 Might points) For the next minute, you gain +1 Armor and an asset to your Might defense "
                    "tasks, as long as you haven’t moved more than an immediate distance since your last turn. Action "
                    "to initiate.",
                "Rally to Me":
                    "(2 Intellect points) You cry out, blow a battle horn, or otherwise signal to everyone within "
                    "very long range that you require aid. All allied creatures who respond by moving to within an "
                    "immediate distance of you within the next few rounds gain one asset on any one attack or defense "
                    "task within the next hour that you suggest, such as “hold the gate,” “charge that group of "
                    "abhumans,” or something similar. Action to initiate.",
            },
            '2': {
                "Mind for Might":
                    "When performing a task that would normally require spending points from your Intellect Pool, "
                    "you can spend points from your Might Pool instead, and vice versa. Enabler.",
            },
            '3': {"CHOICE": {
                "Fortification Builder":
                    "Whenever you attempt a crafting task—or help in the crafting task— to build a wall or other "
                    "fortification (regardless of whether it is commonplace or a numenera installation designed as a "
                    "fortification or defense), you lower the assessed difficulty for creating a complex object or "
                    "structure by two steps, to a minimum of difficulty 1. Enabler.",
                "Train Defenders":
                    "During idle moments in the month or more that you’ve been active in an allied community or "
                    "horde, you trained a troop of up to ten level 2 followers. One of their modifications must be "
                    "for tasks related to defending the community from attack. These followers do not accompany you "
                    "when you leave the horde or community, but rather remain behind to see that the community or "
                    "horde remains safe. If you ever use Rally to Me within earshot of your trained defenders, "
                    "each one gains an additional asset each round in tasks related to defending the community. "
                    "Enabler.",
            }},
            '4': {
                "Living Buttress": "You are mightier than others. Add +5 to your Might Pool. Enabler.",
            },
            '5': {
                "Reinforcing Field":
                    "(6+ Intellect points) You can reinforce any object or structure by infusing it with a force "
                    "field for one hour. The force field increases the level of the object or structure by 2 for "
                    "tasks related to durability and withstanding damage and destruction. Action to initiate.",
            },
            '6': {"CHOICE":{
                "Generate Force Field":
                    "(9+ Intellect points) You create six planes of solid force (level 8), each 30 feet (9 m) to a "
                    "side, which persist for one hour. The planes must be contiguous, and they retain the position "
                    "that you choose when initiating the special ability. For instance, you could arrange the planes "
                    "linearly, creating a wall 180 feet (55 m) long, or you could create a closed cube. The planes "
                    "conform to the space available. Each additional level of Effort you apply increases the level of "
                    "the barrier by one (to a maximum of level 10) or increases the number of hours it remains by "
                    "one. Action to initiate.",
                "Rout Horde":
                    "(9+ Intellect points) With a display of energy, force, and shaking earth, you can attempt to "
                    "rout a horde of up to rank 2 for one hour (or potentially longer if the horde has second "
                    "thoughts about pressing its attack). A routed horde retreats several hundred yards and assesses "
                    "its options. For each level of Effort you apply, you can attempt to affect a horde whose rank is "
                    "one higher. Action to initiate.",
            }}
        },
    },
    "Defends the Weak": {
        "Description": "Someone has to stand up for the helpless, the weak, and the unprotected. You believe this "
                       "duty falls to you, and thus you have spent much of your life watching out for the people "
                       "around you. When you see them in trouble, you are the first to come to their aid. You might "
                       "give up your last shin to help the hungry, take a beating to save a person from the same, "
                       "or rally your friends to take on injustice wherever you find it.",
        "Connection": [
            "Pick one other PC. You failed to protect this character at some point in the past, and you feel compelled "
            "to make up for your failure.",
            "Pick one other PC. This character claimed innocence during a long-ago event, and you protected them. Now "
            "that time has passed, you’re not entirely convinced that they were blameless.",
            "Pick two other PCs. They seem to think that you are more of an arbitrator than you really are, and they "
            "keep asking you to choose which one of them is correct.",
            "Pick one other PC. They believe that one of the tokens of gratitude you carry came from their father.",
        ],
        "Additional Equipment": {
            "Equipment": ["a shield"]
        },
        "Core Features": {},
        "Major Effect Suggestions": "You can take an extra action, though you can use this action only to stand guard.",
        "Minor Effect Suggestions": "You can draw an attack without having to use an action at any point before the "
                                    "end of the next round.",
        "Tiers": {
            '1': {
                "Courageous": "You are trained in Intellect defense tasks and initiative tasks. Enabler.",
                "Warding Shield": "You have +1 to Armor while you are using a shield. Enabler.",
            },
            '2': {
                "Devoted Defender":
                    "(2 Might or Intellect points) Choose one character you can see. That character becomes your "
                    "ward. You are trained in all tasks involving finding, healing, interacting with, and protecting "
                    "that character. You can have only one ward at a time. Action to initiate.",
                "Insight":
                    "You are trained in tasks to discern others’ motives and to ascertain their general nature. You "
                    "have a knack for sensing whether or not someone is truly innocent. Enabler.",
            },
            '3': {"CHOICE": {
                "Dual Wards":
                    "You can have two wards from Devoted Defender at a time. Choosing a second ward can be its own "
                    "action, or you can choose two wards with one action (and only pay the cost once for doing so). "
                    "The wards must remain within an immediate distance of each other. Benefits provided by Devoted "
                    "Defender apply to both your wards. If your wards separate, you choose which retains the benefit. "
                    "If they come back together, both regain the benefit immediately. Enabler.",
                "True Guardian":
                    "(2 Might or Intellect points) When you stand guard as your action, allies within immediate range "
                    "of you gain an asset to their defense tasks. This lasts until the end of your next turn. "
                    "Enabler.",
            }},
            '4': {
                "Combat Challenge":
                    "All attempted tasks that draw an attack to yourself (and away from someone else) are eased by "
                    "two steps. Enabler.",
                "Willing Sacrifice":
                    "When you take an attack meant for another character, you know how to take the attack in a way "
                    "that minimizes its effect. The attack automatically strikes you, but instead of taking 1 "
                    "additional point of damage, you take 1 less point of damage (to a minimum of 1 point). "
                    "Additionally, you can take more than one attack in a given round provided all the attacks were "
                    "originally meant for one target. Enabler.",
            },
            '5': {
                "Taunt Foe":
                    "(4 Might or Intellect points) You can make an attack on a foe as part of drawing an attack ("
                    "which is not something you can do normally when attempting to draw an attack). In cases where an "
                    "intelligent or determined foe isn’t drawn to you, you can attempt an Intellect action as part of "
                    "the attack. If that Intellect action is successful, the foe attacks you. Your defenses against "
                    "that attack are hindered by one step, instead of being hindered by two steps as normal when "
                    "drawing an attack. Enabler.",
            },
            '6': {"CHOICE": {
                "Resuscitate":
                    "(6 Intellect points) You can resuscitate a character who is up to two steps down on the damage "
                    "track as your action. The target ascends one step on the damage track. If a character has "
                    "dropped all three steps on the damage track (dead) but is otherwise in one piece and less than a "
                    "minute has passed since they descended the third step, you can resuscitate them if you succeed "
                    "at a level 6 healing task. If you use this ability on an NPC who has no health but is otherwise "
                    "in one piece, the NPC is resuscitated with 1 health. Action.",
                "True Defender":
                    "(6 Might or Intellect points) This ability functions as the Devoted Defender ability, except the "
                    "benefit applies to up to three characters you choose. If you choose just one character, "
                    "you become specialized in the tasks described under the Devoted Defender ability. Action to "
                    "initiate.",
            }}
        },
    },
    "Descends From Nobility": {
        "Description": "You descend from privilege, wealth, and power. Your family once owned land (perhaps they "
                       "still do), wielded political control, and accumulated vast wealth. You’ve stepped away from "
                       "that somewhat, though you still carry a noble title, whether you want it or not. People "
                       "sometimes recognize your name, and sometimes they recognize you as being descended from "
                       "nobility. But with many areas being so isolated from each other, people in an area far from "
                       "where you came from may never even have heard of the place where your family is known.",
        "Connection": [
            "Pick one other PC. This character was once in service to your parents’ household, but you have since "
            "grown to think of them as a peer.",
            "Pick one other PC. You’re pretty sure that they are descended from a rival house, even if they don’t know "
            "it.",
            "Pick one other PC. You used your nobility—your influence, your wealth, or the promise of a favor—to "
            "intercede on this character’s behalf.",
            "Pick one other PC. You were once very close with this character in the distant past.",
        ],
        "Additional Equipment": {},
        "Core Features": {
            "Noble Advantage":
                "If you wish, you can swap an ability gained from your type for the following. \nServant. Your name "
                "entitles you to a level 2 follower. One of their modifications must be for tasks related to serving "
                "as your personal assistant. You can ask your servant to deliver things for you, run messages, "
                "pick up objects of interest or items on a list—pretty much whatever you want, within reason. They "
                "can also run interference if you’re trying to avoid someone, help hide you from the attention of "
                "others, help you muscle through a crowd, and so on. Enabler.",
        },
        "Major Effect Suggestions": "The foe is influenced, captivated, or otherwise affected by your ability for "
                                    "twice as long as normal.",
        "Minor Effect Suggestions": "The next time you attempt to command, captivate, or otherwise influence the same "
                                    "foe, the task is eased.",
        "Tiers": {
            '1': {
                "Privileged Nobility":
                    "You are adept at claiming the rewards that a noble background can generate. When recognized, "
                    "you can be seated at any eating establishment no matter how full, get a room in an inn even if "
                    "that means others are turned out, be let into any court or other structure where laws are "
                    "decided or nobility rules, be invited to any gala, and get a seat at a private function of any "
                    "sort. In addition, you are trained in persuasion. Enabler.",
            },
            '2': {
                "Trained Interlocutor":
                    "Through wit, charm, humor, and grace (or sometimes rudeness, threatening posture, "
                    "and obscenity), you’re better able to talk others into what you want. You are trained in all "
                    "interactions. Enabler.",
            },
            '3': {"CHOICE":{
                "Command":
                    "(3 Intellect points) Through sheer force of will, you can issue a simple imperative command to a "
                    "single living creature, who then attempts to carry out your command as its next action. The "
                    "creature must be within short range and able to understand you. The command can’t inflict "
                    "direct harm on the creature or its allies, so “Commit suicide” won’t work, but “Flee” might. In "
                    "addition, the command can require the creature to take only one action, so “Unlock the door” "
                    "might work, but “Unlock the door and run through it” won’t. A commanded creature can still "
                    "defend itself normally and return an attack if one is made on it. If you possess a type ability "
                    "that allows you to command a creature, you can target two creatures at once as your base effect "
                    "if you use either ability. Action.",
                "Noble’s Courage":
                    "(3+ Intellect points) Your noble lineage teaches that courage is necessary to do things that are "
                    "difficult, tedious, or dangerous. When your mind would be negatively affected by an effect of up "
                    "to level 4, whether something as overt as a psychic command or illness or something as subtle as "
                    "fear or even boredom, your courage neutralizes the effect for up to a minute or, if actively "
                    "being attacked, until the next attack. For each level of Effort applied, you can increase the "
                    "level of the effect you can neutralize by 1. Enabler.",
            }},
            '4': {
                "Retinue":
                    "Four additional level 2 followers join you (and your first servant, if you have one). One of "
                    "their modifications must be for tasks related to serving as your personal assistants. In "
                    "addition to other tasks they might individually take on your behalf, they can also work together "
                    "to run interference if you’re trying to avoid someone, help hide you from the attention of "
                    "others, help you muscle through a crowd, and so on. If a situation becomes physically violent, "
                    "they provide an asset to your Speed defense tasks and, if you command it, try to hold a foe’s "
                    "attention while you escape. Enabler.",
            },
            '5': {
                "Asserting Your Privilege":
                    "(3 Intellect points) Acting as only a privileged noble can, you verbally harangue a foe who can "
                    "hear you so forcefully that they are unable to take any action, including attacks, "
                    "for one round. Whether you succeed or fail, the difficulty of the next action the target takes "
                    "is hindered. Action.",
            },
            '6': {"CHOICE": {
                "Font of Inspiration":
                    "(7 Intellect points) An allied character within immediate range gains a free level of Effort on "
                    "their next turn. Once this ability is used, others can’t gain inspiration from you again until "
                    "after you make a recovery roll. Action.",
                "Mind of a Ruler":
                    "(6 Intellect points) When you develop a course of action to deal with a future situation, "
                    "you can ask the GM one very general question about what is likely to happen if you carry out the "
                    "plan, and you will get a simple, brief answer. Action.",
            }}
        },
    },
    "Emerged From The Obelisk": {
        "Description": "There is a gap in your memory lasting well over a year. One moment, you were marveling at the "
                       "appearance of a floating obelisk. The next, you were waking up in a shallow crater, "
                       "being helped up by a traveler. They witnessed you emerging from the side of that same "
                       "obelisk, then falling and smiting the ground. Instead of dying, you made a crater, "
                       "because your body was somehow changed and had become crystalline.",
        "Connection": [
            "Pick one other PC. When your appearance raises concerns among other people who don’t know you, "
            "this character seems interested in giving you support and knowledge to help you fit in.",
            "Pick one other PC. They saw you emerge from the obelisk and came to your aid.",
            "Pick one other PC. They saw you emerge from the obelisk but thought you were a numenera device to be "
            "salvaged, which is how you got off on the wrong foot. It’s up to you whether you still hold a grudge.",
            "Pick one other PC. In the past, this character has indulged you by listening to you wonder about your "
            "origins, how to get into obelisks, and why you might have been ejected.",
        ],
        "Additional Equipment": {
            "Equipment": ["A 1-pound (450 g) chunk of inert amber crystal"]
        },
        "Core Features": {},
        "Major Effect Suggestions": "Your foe loses their next turn.",
        "Minor Effect Suggestions": "Your foe is dazed for one round, during which time all their tasks are hindered.",
        "Tiers": {
            '1': {
                "Crystalline Body":
                    "You are composed of animate, translucent crystal the color of amber. Work with your GM to decide "
                    "your exact form, though it is likely about the shape and size of a humanoid. Your crystal body "
                    "grants you +2 to Armor and +4 to your Might Pool. However, you’re not quick and your Speed "
                    "defense tasks are hindered. Certain conditions, like mundane diseases and poisons, do not affect "
                    "you. Enabler.",
                "Special Healing":
                    "Your crystalline body repairs itself more slowly than that of living flesh. You  have only the "
                    "one-round, one-hour, and ten- hour recovery rolls available each day; you do  not have a "
                    "ten-minute recovery roll available. Any ability you have that requires a ten-minute recovery "
                    "roll instead requires a one-hour recovery roll. Enabler.",
            },
            '2': {
                "Amber Levitation":
                    "(3+ Intellect points) You learn how to energize your crystalline form and lift away from the "
                    "pull of gravity. You can levitate an immediate distance in any direction each round for up to a "
                    "minute. Each level of Effort applied allows you to lift one other creature of up to your size, "
                    "assuming they can come up with some way to secure themselves to you. Action to initiate.",
            },
            '3': {"CHOICE": {
                "Inhabit Crystal":
                    "(4 Intellect points) You transfer your body and whatever you are carrying into a crystal at "
                    "least the size of your index finger. While in the crystal, you are aware of what is going on "
                    "around it, seeing and hearing through the crystal. You can even speak through the crystal and "
                    "carry on conversations. You cannot take actions other than to exit the crystal. You remain "
                    "within as long as you wish, but you are not in stasis and should exit to eat, drink, sleep, "
                    "and so on as normal (breathing is not an issue). If the crystal is destroyed or takes major "
                    "damage while you are within it, you immediately exit, cannot act for three rounds, and move two "
                    "steps down the damage track. Action to enter and exit.",
                "Immovable":
                    "You can attempt a Might task to avoid being knocked down, pushed back, or moved against your "
                    "will even if the effect attempting to move you doesn’t allow it. If you apply Effort to this "
                    "task, you can apply two free levels of Effort. In addition, you gain +3 to your Might Pool. "
                    "Enabler.",
            }},
            '4': {
                "Crystal Lens":
                    "You can focus the inherent energy surging through your crystalline body. This allows you to fire "
                    "a blast of energy that inflicts 5 points of damage at a target within very long range. Action.",
            },
            '5': {
                "Resonant Frequency":
                    "You can infuse an item of up to level 7 that you can hold in one hand with a special vibration "
                    "generated from your core. The object then functions as if two levels higher for one minute. At "
                    "the end of that minute, the resonant frequency ramps up exponentially until the object finally "
                    "shatters from the energy buildup. Anything within immediate range of the detonation suffers 5 "
                    "points of damage. Action to initiate.",
            },
            '6': {"CHOICE": {
                "Resonant Quake":
                    "(7 Intellect points) You can infuse the ground beneath you with a special vibration generated "
                    "from your core. This creates a small quake whose epicenter you can select within a very long "
                    "distance. Everyone within short range of the epicenter is subject to 8 points of damage (from "
                    "shaking and being struck by toppling objects, crumbling walls, and so on). However, "
                    "you are dazed for a round afterward yourself, during which time all your tasks are hindered. If "
                    "you have the Nano ability Move Mountains, both abilities cost 3 fewer Intellect points to use. "
                    "Action.",
                "Return to the Obelisk":
                    "(7+ Intellect points) You transfer your body and personal possessions into a crystal of any size "
                    "and exit from another crystal of any size, including any crystal obelisks that you are aware of. "
                    "You must know of the crystal you are going to use as an exit before you enter the first crystal. "
                    "You can take one additional creature with you for each level of Effort applied. Action.",
            }}
        },
    },
    "Explores Yesterday": {
        "Description": "What things were like long ago fires your imagination. You are equally thrilled to learn "
                       "about how a dead civilization lived as you are to regain a still-functioning oddity, cypher, "
                       "or iotum that the dead civilization used. For you, knowledge is an end in itself, "
                       "but that doesn’t make you naive to the dangers exploration poses. The opposite is true, "
                       "which is why you’re no slouch when it comes to defending yourself. You’re a born excavator "
                       "and explorer, adept at moving and maneuvering, making discoveries, and resisting the dangers "
                       "that forgotten places often hold.",
        "Connection": [
            "Pick one other PC. This character has been your partner in previous explorations, and the two of you "
            "work so well together that you both gain +1 to any roll when you collaborate on the same task, "
            "fight the same foe, and so on.",
            "Pick one other PC. This character nearly drowned while following you on one of your excavations. It’s up "
            "to them whether they trust you enough to go exploring with you again.",
            "Pick one other PC. They suspect that you were involved with criminals who stole from the Amber Gleaners. "
            "Whether you were or not is up to you.",
            "Pick one other PC. You suspect this character possesses secret knowledge of a hidden tomb, lost city, or "
            "treasure. Whether they really do or not remains up to them to decide.",
        ],
        "Additional Equipment": {
            "Equipment": ["a bag of excavation tools."]
        },
        "Core Features": {},
        "Major Effect Suggestions": "Speed defense tasks you attempt before the end of the next round are eased.",
        "Minor Effect Suggestions": "You can take an extra action. You may use this action only to perform a "
                                    "movement-related activity or a knowledge-based activity, such as trying to climb "
                                    "a treacherous cliff or attempting to decipher strange cave markings.",
        "Tiers": {
            '1': {
                "Trained Excavator": "You are trained in perception, climbing, and salvaging numenera tasks. Enabler.",
            },
            '2': {
                "Resilient":
                    "In your explorations of uncivilized regions, you’ve been exposed to all sorts of terrible things "
                    "and have developed a general resistance. You gain +1 to Armor and are trained in Might defense "
                    "tasks. Enabler.",
            },
            '3': {"CHOICE":{
                "Fellow Explorer":
                    "You gain a level 2 follower. One of their modifications must be for tasks related to perception. "
                    "Enabler.",
                "Weapon Master":
                    "Excavating the past means entering ruins that are often filled with dangers, some of which can "
                    "be overcome by force. Choose one kind of weapon you can use. You gain a +1 bonus to damage with "
                    "that weapon. Enabler.",
            }},
            '4': {
                "Got a Feeling":
                    "(4 Intellect points) Your experience excavating the ruins of the prior worlds gives you an "
                    "uncanny intuition when it comes to finding things. While exploring, you can extend your senses "
                    "up to 1 mile (1.5 km) in any direction and ask the GM a very simple, general question—usually a "
                    "yes-or-no question—about that area, such as “Is there an abhuman encampment nearby?” or “Is "
                    "there iotum to be found in that rusted hulk?” If the answer you seek is not in the area, "
                    "you receive no information. Action.",
            },
            '5': {
                "Maneuvering Adept":
                    "If you apply at least one level of Effort to a task involving climbing, jumping, balancing, "
                    "or some other kind of maneuvering, you get a free level of Effort. Enabler.",
            },
            '6': {"CHOICE": {
                "Incredible Recovery":
                    "(6 Might points) You move up one step on the damage track or shake off any unwanted ongoing "
                    "condition. Action.",
                "Quick Hands":
                    "(5 Speed points) Being quick with a chosen weapon is important for excavators who come across an "
                    "unexpected and aggressive threat. Choose one kind of weapon you can use (if you have the Weapon "
                    "Master ability, this can be the same kind of weapon that you chose for Weapon Master). Once per "
                    "round, you can make an additional attack with it. Make separate attack rolls for each foe, "
                    "but both attacks count as a single action in a single round. You remain limited by the amount of "
                    "Effort you can apply on one action. Anything that modifies your attack or damage applies to both "
                    "of these attacks. Enabler.",
            }}
        },
    },
    "Fights with a Hoarde": {
        "Description": "You were once part of a much larger martial society, where you held a position of elevated "
                       "respect. The society might have been a tribe of abhumans, a military unit, a secret group of "
                       "warriors that live in a limited dimension, or something else. Whatever the specifics (which "
                       "you and your GM should work together to decide), you formed close personal ties with them and "
                       "trained to fight in small and large groups alike. But at some point, you left, perhaps to "
                       "seek your destiny, because you were exiled, or because everyone in the society spends a "
                       "significant time away before returning to retire. Though you are gone, the lessons of "
                       "teamwork and leadership that you learned while part of that society remain with you.",
        "Connection": [
            "Pick one other PC. You’re related, either siblings or cousins, but were separated when you were young.",
            "Pick one other PC. They’re a good fighter, but if you could teach them a few things about working "
            "together, they’d improve.",
            "Pick one other PC. This character doesn’t seem to approve of your past association.",
            "Pick one other PC. Long ago, the two of you were on opposite sides of a fight. You won, thanks to your "
            "association with your martial society. Whether they remember you or still hold a grudge is up to them.",
        ],
        "Additional Equipment": {
            "Equipment": ["melee weapon you gained from your association with the martial society with their symbol or "
                          "crest on the hilt"]
        },
        "Core Features": {},
        "Major Effect Suggestions": "Your foe is held immobile and can’t take their next turn.",
        "Minor Effect Suggestions": "Your foe is knocked to the ground.",
        "Tiers": {
            '1': {
                "Teamwork":
                    "Through example, acts of camaraderie, stories of martial prowess, or other forms of instruction, "
                    "you and your allies work better together as a cohesive unit. During any round in which you rally "
                    "your team (by spending 2 Intellect points as part of another action), you and your allies "
                    "inflict 1 additional point of damage in combat. This benefit applies only to allies with whom "
                    "you have spent the last 28 hours. It ends if you leave, but it resumes if you return to your "
                    "allies’ company within 28 hours. If you leave for more than 28 hours, you must spend another 28 "
                    "hours together to reactivate the benefit. Enabler.",
            },
            '2': {
                "Nucleus of a Horde":
                    "One level 3 follower associated with your past martial connection joins you and the rest of your "
                    "allies. One of their modifications must be for providing an asset to attacks or defenses. They "
                    "don’t accompany you everywhere, but you can assign the follower specific tasks like helping you "
                    "guard a community’s perimeter for a day or accompanying you on an expedition. Enabler.",
            },
            '3': {"CHOICE": {
                "Enhance Dexterity":
                    "When the follower from your Nucleus of a Horde ability is near you and working with you to "
                    "accomplish tasks that depend on agility—such as balancing, winning a foot race, or hitting "
                    "someone with a ranged weapon—your follower provides an asset on those tasks, even if those "
                    "aren’t their modifications. Enabler.",
                "Enhance Strength":
                    "When the follower from your Nucleus of a Horde ability is near you and working with you to "
                    "accomplish tasks that depend on brute force—such as moving a heavy object, smashing down a door, "
                    "or hitting someone with a melee weapon—your follower provides an asset on those tasks, "
                    "even if those aren’t their modifications. Enabler.",
            }},
            '4': {
                "Growing Horde":
                    "A group of four additional level 3 followers associated with your past martial connection joins "
                    "you and the rest of your allies (and those gained by Nucleus of a Horde, for a total of five "
                    "followers from your martial society). One of their modifications must be for providing you an "
                    "asset to attacks or defenses. They don’t accompany you everywhere, but you can assign them "
                    "specific tasks like helping you guard a community’s perimeter for a day or accompanying you on "
                    "an expedition. Enabler.",
            },
            '5': {
                "Horde Tactics":
                    "(7 Might points) For up to one hour a day, you and your allies can act like a single creature. "
                    "Use your stats, but add +8 to your Might Pool, +1 to your Might Edge, +2 to your Speed Pool, "
                    "+1 to your Speed Edge, and +1 to your Armor. Alternatively, you and your group can act as a rank "
                    "1 horde for one hour. Enabler.",
            },
            '6': {
                "Advance Rank":
                    "(10 Might points) For the next hour, the rank of any horde you fight with is increased by 1. If "
                    "you have the Glaive ability Rampaging Beast Horde, Advance Rank also applies. Enabler.",
                "Charging Horde":
                    "(7 Might points) You and your followers gained from this focus can act like a single creature to "
                    "make a charge attack. When you do, all of you move up to a short distance, during which time you "
                    "can attack anything that comes within immediate range along your path with an asset to the "
                    "attack. Targets that take damage take an additional 3 points and are knocked prone. Action.",
            }
        },
    },
    "Fuses Mind and Machine": {
        "Description": "You believe that the finest machine ever created is the human brain, and experience and "
                       "training have taught you that any machine can be improved. Through the use of implants and "
                       "mechanical enhancements, your brain processes input faster, stores more information, "
                       "and eventually can tap right into the datasphere. Mentally, you function on an entirely "
                       "different level than your fellows.",
        "Connection": [
            "Pick one other PC. This character knows a few things that can help when your implants and enhancements "
            "malfunction.",
            "Pick one other PC. They seem to find you off-putting. You wonder if it’s because you’re clearly smarter "
            "than they are or if it’s for some other reason.",
            "Pick one other PC. This character has a small device that can shut down your brain with a single switch. "
            "However, you don’t think they have any idea what it is or what it can do.",
            "Pick one other PC. Within your memory circuits, you have data of someone who looks just like this "
            "character committing terrible crimes—hundreds of years ago. You have no explanation.",
        ],
        "Additional Equipment": {
            "an artifact that protects your implants and enhancements from disruption or intrusion. Resisting such "
            "attacks is eased.",
        },
        "Core Features": {},
        "Major Effect Suggestions": "Processing surge! On your next action, you can use points from your Intellect "
                                    "Pool on Might or Speed tasks.",
        "Minor Effect Suggestions": "You foresee your foes’ moves so well that your Speed defense rolls for the next "
                                    "round gain an asset.",
        "Tiers": {
            '1': {
                "Mechanical Assistance":
                    "You gain +4 to your Intellect Pool through the use of implants and tiny processing devices. "
                    "Enabler.",
                "Stored Memories":
                    "You are trained in one area of knowledge of your choice (history, geography, astronomy, "
                    "and so on). Enabler.",
            },
            '2': {
                "Network Tap":
                    "(4 Intellect points) You can ask the GM one question and get a very short answer if you succeed "
                    "on an Intellect roll against a difficulty assigned by the GM. The more obscure the answer, "
                    "the more difficult the task. On a failed roll, feedback or perhaps some defense from the "
                    "datasphere itself inflicts 4 points of Intellect damage on you (ignores Armor). Action.",
            },
            '3': {"CHOICE": {
                "Action Processor":
                    "(4 Intellect points) Drawing upon stored information and the ability to process incoming data at "
                    "amazing speeds, you are trained in one physical task of your choice for ten minutes. For "
                    "example, you can choose running, climbing, swimming, Speed defense, or attacks with a specific "
                    "weapon. Action to initiate.",
                "Machine Telepathy":
                    "(3 Intellect points) You can read the surface thoughts of a machine within short range of you, "
                    "even if the machine doesn’t want you to. You must be able to see the machine. Once you have "
                    "established contact, you can read the target’s thoughts for up to one minute. If you or the "
                    "target move out of range, the connection is broken. If you have the Nano’s Mind Reading ability, "
                    "when you apply Effort to Machine Telepathy, you gain a free level of Effort. Action to initiate.",
            }},
            '4': {
                "Processing Power": "You gain +5 to your Intellect Pool. Enabler.",
                "More Stored Memories":
                    "You are trained in one area of knowledge of your choice (history, geography, astronomy, and "
                    "so on). Enabler.",
            },
            '5': {
                "See the Future":
                    "(6 Intellect points) Based on all the variables you perceive, you can predict the next few "
                    "minutes. This has the following effects: \n* For the next ten minutes, your defense rolls gain an "
                    "asset. \n* You have a sort of danger sense. For the next ten minutes, you gain an asset in seeing "
                    "through deceptions and attempts to betray you, as well as avoiding traps and ambushes. \n* You "
                    "know what people are probably thinking and what they will say before they say it. For the next "
                    "ten minutes, you gain an asset to tasks involving interaction and deception. \nEnabler.",
            },
            '6': {"CHOICE": {
                "Machine Enhancement":
                    "Any time you use Effort on an Intellect action, add one of the following enhancements to the "
                    "action (your choice):\n* A free level of Effort \n* An automatic minor effect \nEnabler. ",
                "Reboot":
                    "In addition to your normal recovery rolls each day, you can—at any time between ten-hour "
                    "rests—recover 1d6 + 10 points to your Intellect Pool. Action.",
            }}
        },
    },
    "Hunts Abhumans": {
        "Description": "Abhumans are a threat to humanity. You know this more than anyone. The threat is obvious— "
                       "bestial abhumans attack villages, caravans, and travelers all the time in the wilderness. But "
                       "the threat is also far subtler. The progenitors of the abhumans were once human. They gave up "
                       "their humanity to become horrific, monstrous things. How this happened, or how long ago, "
                       "are things you cannot conceive. But you know that they are true, so abhumans must be "
                       "eradicated for the good of all.",
        "Connection": [
            "Pick one other PC. This character has had experiences with abhumans in the past, and you’d like to know "
            "more about them.",
            "Pick one other PC. You are friends, and you’d hate to see this character harmed.",
            "Pick one other PC. This character doesn’t understand just how dangerous and horrible abhumans can be.",
            "Pick one other PC. Abhumans are sometimes drawn to certain people. They always seem to attack those "
            "people first and with more fervor. This character appears to be one such person.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "Your foe is terrified by your skill and flees.",
        "Minor Effect Suggestions": "Your foe is so intimidated by your prowess that it backs away, unwilling to "
                                    "attack. It can still defend itself.",
        "Tiers": {
            '1': {
                "Tracker and Hunter":
                    "You are trained in tracking, looking for, interacting with, and hiding from abhumans. Enabler.",
                "Abhuman Fighter": "You inflict 2 additional points of damage when fighting abhumans. Enabler.",
            },
            '2': {
                "Abhuman Sense":
                    "(2 Intellect points) For one hour, through scent, specific signs, and past experience, you know "
                    "when abhumans are within long range. Enabler.",
                "Expert Combatant":
                    "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                    "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, or heavy "
                    "ranged. You are trained in attacks using that type of weapon. Enabler.",
            },
            '3': {"CHOICE": {
                "Answering Attack":
                    "(3 Speed points) If you are struck in melee, you can make an immediate melee attack against that "
                    "attacker once per round. The attack is hindered, and you can still take your normal action "
                    "during the round. Enabler.",
                "Horde Fighting":
                    "When two or more foes attack you at once in melee, you can use them against each other. You gain "
                    "an asset to Speed defense rolls or attack rolls (your choice each round) against them. Enabler.",
            }},
            '4': {
                "Improved Abhuman Fighter":
                    "You inflict 3 additional points of damage when fighting abhumans. Enabler.",
            },
            '5': {
                "Abhuman Slayer":
                    "When fighting abhumans, your attack rolls and defense rolls gain an asset. Enabler.",
            },
            '6': {"CHOICE":{
                "Abhuman Anathema":
                    "When fighting abhumans, you can apply a free level of Effort to all attack rolls and defense "
                    "rolls if you first apply a level of Effort to one of those tasks. Enabler.",
                "Master Combatant":
                    "Choose one type of attack in which you are already trained: light bashing, light bladed, "
                    "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, "
                    "or heavy ranged. You are specialized in attacks using that type of weapon. Enabler.",
            }}
        },
    },
    "Imparts Wisdom": {
        "Description": "You’ve studied philosophy and other higher truths. But you do more than learn about such "
                       "esoteric teachings; you practice them. Every day you consider hard questions or questions "
                       "that everyone else has an easy answer for. That’s just the way you live. By focusing on "
                       "things that bear on life, existence, and the underlying principles that guide the most "
                       "sublime processes in the universe, you know contentment. Others often see in you a teacher, "
                       "a higher being, or perhaps even some sort of savior. However, you see yourself as merely "
                       "another student studying at the feet of eternity.",
        "Connection": [
            "Pick one other PC. This character also yearns for enlightenment. You both gain +1 on any die rolls when "
            "you collaborate on the same task, fight the same foe, and so on.",
            "Pick two other PCs. You have seen them, or someone who looked like them, stray from the path of wisdom "
            "before you became allies. You can choose whether or not to share that information. These characters can "
            "choose whether it was really them (it might not have been), and they may or may not share that "
            "information in return.",
            "Pick one other PC. This character never seems to learn from you, and you both gain –1 on any die rolls "
            "when you collaborate on the same task, fight the same foe, and so on.",
            "Pick one other PC. This character is so wrong in everything that you feel obligated to try to help them "
            "better understand the world. Whether or not the character is interested is up to them.",
        ],
        "Additional Equipment": {},
        "Core Features": {
            "Wisdom Benefits":
                "If you wish, you can swap an ability gained from your type for the following. \nPhilosophic Confusion:"
                "\n(1 Intellect point) Your esoteric words confuse a creature that can understand you, making it "
                "stand without taking actions as it attempts to pierce the puzzle set before it. For as long as you "
                "do nothing but pontificate (you can’t even move), the other creature takes no actions other than to "
                "defend itself, even over multiple rounds. If the creature is attacked, the effect ends. If you have "
                "a type ability that accomplishes the same thing, you can attempt to use either ability on two "
                "creatures at a time. Action. "
            ,
        },
        "Major Effect Suggestions": "Intuition flares, and you can ask the GM one question about what you’re looking "
                                    "at.",
        "Minor Effect Suggestions": "You don’t have to use an action ahead of time to use your next Learning the Path "
                                    "or Imparting the Path ability.",
        "Tiers": {
            '1': {
                "Learning the Path":
                    "(2 Intellect points) You observe or study a creature, object, or location for at least one "
                    "round. The next time you interact with it (possibly in the following round), a related task ("
                    "such as persuading the creature, attacking it, or defending from its attack) is eased. Action.",
                "Philosophy": "You are trained in two areas of knowledge of your choice.",
            },
            '2': {
                "Imparting the Path":
                    "Through example, teaching, and frank speech about piercing what only seems to be mysterious in "
                    "the world, you impart wisdom to your allies. After spending 28 hours with you, each of your "
                    "friends can ease one task once per day. This benefit is ongoing while you remain in the friend’s "
                    "company. It ends if you leave, but it resumes if you return to the friend’s company within 28 "
                    "hours. If you leave the friend’s company for more than 28 hours, you must spend another 28 hours "
                    "together to reactivate the benefit. Enabler.",
            },
            '3': {"CHOICE":{
                "Genius":
                    "The more you accumulate wisdom, the sharper your mind becomes. You gain +5 to your Intellect "
                    "Pool. Enabler.",
                "Soothe Mind and Body":
                    "The body and the mind are connected. All healing tasks you attempt are eased by two steps. "
                    "Enabler.",
            }},
            '4': {
                "Inspire Action":
                    "(4 Intellect points) If one ally can see and easily understand you, you can instruct that ally "
                    "to take an action. If the ally chooses to take that exact action, they can take it as an "
                    "additional action immediately. Doing so doesn’t interfere with the ally taking a normal action "
                    "on their turn. If you have the Arkus ability of the same name, when you use either ability, "
                    "you can also move up to a short distance as part of the same action. Action.",
            },
            '5': {
                "Change the Paradigm":
                    "(6+ Intellect points) You sway the worldview of a creature you spend at least one round speaking "
                    "to, as long as it can understand you. The creature changes its mind on some significant belief, "
                    "which could include something as straightforward as helping you instead of trying to kill you, "
                    "or it could be something more esoteric. This effect lasts for at least ten minutes, but it can "
                    "last longer if the creature wasn’t previously your foe. During this time, the creature takes "
                    "actions in accordance with the wisdom you have imparted to it. The target must be level 2 or "
                    "lower. In addition to the normal options for using Effort, you can also choose to use Effort to "
                    "increase the maximum level of the target by one for each level applied. Action to initiate.",
            },
            '6': {"CHOICE":{
                "Impart Understanding":
                    "Your Learning the Path ability works more effectively, allowing you to ease a task by two steps "
                    "or to provide two assets to a friend’s task, instead of easing normally. Enabler.",
                "Undo":
                    "(5 Intellect points) What just happened isn’t what actually happened; it was a thought "
                    "experiment. Knowing better, you can effectively undo a single creature’s most recent action. "
                    "That creature can then immediately repeat the same action or try something different. Action.",
            }}
        },
    },
    "Leads": {
        "Description": "Using charisma, natural leadership, and perhaps some training, you command the actions of "
                       "others, who follow you willingly. You are a commander, a captain, a leader, or a general. "
                       "Your skills allow you to make people do what you want, but you also have the wisdom to know "
                       "what actions would be best for your followers and allies.",
        "Connection": [
            "Pick one other PC. This character was once a follower of yours, but you have since grown to think of "
            "them as a peer.",
            "Pick one other PC. Independent and stubborn, they are not affected by your abilities.",
            "Pick one other PC. They introduce you to the follower you gain at tier 2.",
            "Pick one other PC. You were once very close with this character in the distant past.",
        ],
        "Additional Equipment": {
            "Artefact":
                ["an artifact that allows you to tag up to seven followers. By looking into the glass plate on the "
                 "device, you can determine their distance and direction relative to you. The tagging process is "
                 "somewhat demeaning, so it is likely that only your followers would ever submit to it."],
        },
        "Core Features": {},
        "Major Effect Suggestions": "The foe is influenced, captivated, or otherwise affected by your ability for "
                                    "twice as long as normal.",
        "Minor Effect Suggestions": "The next time you attempt to command, captivate, or otherwise influence the same "
                                    "foe, the task is eased.",
        "Tiers": {
            '1': {
                "Natural Charisma":
                    "You are trained in all social interactions, whether they involve charm, learning a person’s "
                    "secrets, or intimidating others. Enabler.",
                "Good Advice":
                    "Anyone can help an ally, easing whatever task they’re attempting. However, you have the benefit "
                    "of clarity and wisdom. When you help another character, they gain an additional asset. Enabler.",
            },
            '2': {
                "Lead From the Front":
                    "No one is going to allow themselves to be governed by someone not willing to lay it on the line "
                    "themselves. Thus, you constantly test yourself, and this toughens you. You gain +3 to your Might "
                    "Pool. Enabler.",
                "Follower":
                    "You gain a level 2 follower. They are not restricted on their modifications other than the "
                    "general restriction that followers of level 2 and lower cannot grant an asset to a character’s "
                    "attacks or defense. Enabler.",
            },
            '3': {"CHOICE": {
                "Command":
                    "(3 Intellect points) Through sheer force of will and charisma, you issue a simple command to a "
                    "single living creature, which attempts to carry out your command as its next action. The "
                    "creature must be within short range and be able to understand you. The command can’t inflict "
                    "direct harm on the creature or its allies, so “Commit suicide” won’t work, but “Flee” might. In "
                    "addition, the command can require the creature to take only one action, so “Unlock the door” "
                    "might work, but “Unlock the door and run through it” won’t. A commanded creature can still "
                    "defend itself normally and return an attack if one is made on it. If you possess a type ability "
                    "that allows you to command a creature, you can target two creatures at once as your base effect "
                    "if you use either ability. Action.",
                "Improved Follower":
                    "You gain a level 3 follower. They are not restricted on their modifications. You can take this "
                    "ability multiple times, each time gaining another level 3 follower. Enabler.",
            }},
            '4': {
                "Captivate or Inspire":
                    "You can use this ability in one of two ways. Either your words keep the attention of all NPCs "
                    "that hear them for as long as you speak, or your words inspire all NPCs that hear them to "
                    "function as if they were one level higher for the next hour. In either case, you choose which "
                    "NPCs are affected. If anyone in the crowd is attacked while you’re trying to speak to them, "
                    "you lose the crowd’s attention. Action to initiate.",
            },
            '5': {
                "Confidence":
                    "Leaders inspire confidence, and confidence comes from real ability. You gain 6 new points to "
                    "divide among your stat Pools however you wish. Enabler.",
            },
            '6': {"CHOICE":{
                "Band of Followers":
                    "You gain four level 3 followers. They are not restricted on their modifications. Enabler.",
                "Mind of a Leader":
                    "(6 Intellect points) When you develop a plan that involves your followers, you can ask the GM "
                    "one very general question about what is likely to happen if you carry out the plan, and you will "
                    "get a simple, brief answer. Action.",
            }}
        },
    },
    "Learns From Adversity": {
        "Description": "You’ve been around, which means that you’ve experienced the pendulum swings that living "
                       "delivers to every creature. No matter the heights that someone might attain, situations "
                       "change, disasters happen, friends die, and mistakes are made. No matter how brilliant you "
                       "might be, or believe yourself to be, those mistakes are often made by you. What distinguishes "
                       "you from others is that you learn from those mistakes. You learn from the past and use "
                       "experience as your guide. You’re older than many, but you’ve seen some amazing things in that "
                       "time, and you can draw on that experience to do amazing things.",
        "Connection": [
            "Pick one other PC. You languished in some kind of terrible situation until this character plucked you "
            "out of it. You learned a lot from that experience.",
            "Pick one other PC. They don’t seem to think much of your experience.",
            "Pick one or more other PCs. They came looking for help with a problem and found you. It’s up to them "
            "whether they’re satisfied with what they found or not.",
            "Pick one other PC. This character believes  you’re some kind of legend based on a decade- old story about "
            "you that’s grown in the telling.  Sometimes, that makes you confident. Other times, it’s a lot to live up "
            "to.",
        ],
        "Additional Equipment": {
            "Equipment": ["book filled with knowledge on a topic of your choice"]
        },
        "Core Features": {},
        "Major Effect Suggestions": "You can take another action on the same turn.",
        "Minor Effect Suggestions": "The range or duration of one of your abilities is doubled.",
        "Tiers": {
            '1': {
                "Quicker Than Most":
                    "Experience has honed your reaction times, because those who act first gain the advantage in most "
                    "situations. You’re trained in tasks related to initiative, seeing underlying patterns, "
                    "and solving puzzles. Enabler.",
                "Toughened Up":
                    "Adversity has made you tougher. You gain +3 to your Might Pool. Enabler.",
            },
            '2': {
                "Inner Defense":
                    "Life’s trials have toughened you and made you hard to read. You are trained in any task to "
                    "resist another creature’s attempt to discern your true feelings, beliefs, or plans. You are "
                    "likewise trained in resisting torture, telepathic intrusion, and mind control. Enabler.",
                "Mental Fortitude":
                    "Your mind is stronger for overcoming bad experience. You gain +3 to your Intellect Pool. Enabler.",
            },
            '3': {"CHOICE": {
                "Know Their Faults":
                    "You don’t live as long as you have without learning what makes others tick. If a creature that "
                    "you can see has a special weakness, such as a vulnerability to loud noises, a negative "
                    "modification to perception, and so on, you know what it is. Ask and the GM will tell you; "
                    "usually, this is not associated with a roll, but in certain cases the GM may decide that there "
                    "is a chance for you not to know. In these cases, you are specialized in knowing creature "
                    "weaknesses. Enabler.",
                "Tall Tale":
                    "(3 Intellect points) You tell a short anecdote to a foe that can understand you about something "
                    "you’ve witnessed in your life that’s so over the top yet so convincing that, if you are "
                    "successful, the foe is dazed for one minute, during which time its tasks are hindered. Action.",
            }},
            '4': {
                "Seize Opportunity":
                    "(4 Speed points) You’ve learned that you have to react instantly when danger threatens. Once per "
                    "round, if you succeed on a Speed defense roll to resist an attack, you gain an action. You can "
                    "use it immediately even if you have already taken a turn in the round. If you use this action to "
                    "attack, your attack is eased. You don’t take an action during the next round. Enabler.",
            },
            '5': {
                "Twist of Fate":
                    "Experience has taught you a lot, including that luck is sometimes something that you have to "
                    "make for yourself. When you roll a 1, you can reroll. You must use the new result, even if it’s "
                    "another 1. Enabler.",
                "Expeditious":
                    "Learning from adversity includes recognizing when to move quickly. You gain +3 to your Speed "
                    "Pool. Enabler.",
            },
            '6': {"CHOICE":{
                "Exploit Advantage":
                    "Even if you can do something well, you’ve learned that you can always do it even better. "
                    "Whenever you have an asset for a roll, you ease the task by one additional step. Enabler.",
                "Lethal Ploy":
                    "(5+ Intellect points) Long experience has revealed to you that subterfuge is your friend in "
                    "desperate situations. You push, attack, or distract the target in some seemingly inconsequential "
                    "way that leads to the target’s death. The target must be level 2 or lower. In addition to the "
                    "normal options for using Effort, you can also choose to use Effort to increase the maximum level "
                    "of the target by 1. Thus, to kill a level 5 target (three levels above the normal limit), "
                    "you must apply three levels of Effort. Action.",
            }}
        },
    },
    "Metes Out Justice": {
        "Description": "There is so much injustice in the world. It takes a special person to take it upon himself to "
                       "right wrongs, protect the innocent, and punish the guilty. You are such a person. "
                       "\nJusticars, as they are sometimes called, are knights errant who wear armor, bear swords and "
                       "shields, and travel the land looking for tyranny, corruption, and oppression. But some "
                       "operate a little less ostentatiously, and sometimes justice comes from more subtle tactics. A "
                       "justicar might also be a masked vigilante or just a badass who rights wrongs.",
        "Connection": [
            "Pick one other PC. You strongly suspect that this character has a past that might involve serious crimes "
            "or wrongdoing. You have no proof, however, and you’ve never witnessed them doing anything seriously "
            "wrong.",
            "Pick one other PC. This character seems to share your value systems and sees right and wrong the same way "
            "you do, which is refreshing.",
            "Pick one other PC. This character, while ethical, defines right and wrong in different ways than you do.",
            "Pick one other PC. In the past, you and this character witnessed an event that helped shape your moral "
            "code. They may or may not have come away with a similar outlook.",
        ],
        "Additional Equipment": {"Equipment": ["a shield"]},
        "Core Features": {},
        "Major Effect Suggestions": "You mark your foe permanently with a distinctive scar so that their guilt will "
                                    "be known by all.",
        "Minor Effect Suggestions": "You shame or intimidate your foe so much that they are shaken and use their next "
                                    "turn to flee.",
        "Tiers": {
            '1': {
                "Make Judgment":
                    "You are trained in discerning the truth of a situation, seeing through lies, or otherwise "
                    "overcoming deception. Enabler.",
                "Designation":
                    "You assign an innocent or guilty label to one creature within immediate range, based on your "
                    "assessment of a given situation or a predominant feeling. In other words, someone who is labeled "
                    "innocent can be innocent in a certain circumstance, or they can be generally innocent of "
                    "terrible crimes (such as murder, major theft, and so on). Likewise, you can declare that a "
                    "creature is guilty of a particular crime or of terrible deeds in general. The accuracy of your "
                    "assessment isn’t important as long as you believe it to be the truth; the GM may require you to "
                    "give a rationale. Henceforth, your tasks to socially interact with someone you designate as "
                    "innocent gain an asset, and your attacks against those you designate as guilty gain an asset. "
                    "You can change your assessment, but it requires another designation action. The benefits of the "
                    "designation last until you change it or until you are shown proof that it is wrong. Action.",
            },
            '2': {
                "Defend the Innocent":
                    "(2 Speed points) For the next ten minutes, if someone you have designated as innocent stands "
                    "next to you, that creature shares any defensive advantages that you might have, other than "
                    "mundane armor. These advantages include the Speed defense from your shield, the Armor offered "
                    "from a force field, and so on. In addition, Speed defense rolls made by the innocent creature "
                    "gain an asset. You can protect only one innocent creature at a time. Action to initiate.",
                "Improved Designation":
                    "You can designate one additional creature to be innocent or guilty when you use Designation, "
                    "which means up to two creatures at a time may be innocent, or two guilty, or one innocent and "
                    "one guilty. Enabler.",
            },
            '3': {"CHOICE": {
                "Defend All the Innocent":
                    "You protect everyone within immediate range whom you have designated as innocent. Speed defense "
                    "rolls made by such creatures gain an asset. Enabler.",
                "Punish the Guilty":
                    "(2 Might points) For the next ten minutes, if you attack someone you have designated as guilty, "
                    "you inflict 2 additional points of damage. Action to initiate.",
            }},
            '4': {
                "Find the Guilty":
                    "If you have designated someone as guilty, you are trained in tracking them, spotting them when "
                    "they are hidden or disguised, or otherwise finding them. Enabler.",
                "Greater Designation":
                    "You can assign an innocent or guilty label to all creatures within immediate range when you use "
                    "Designation. The one label applies to all affected creatures. This lasts until you use Greater "
                    "Designation again. Action.",
            },
            '5': {
                "Punish All the Guilty":
                    "(3 Speed points) You can attack up to five foes within immediate range that you have designated "
                    "as guilty, all as part of the same action in one round. Make separate attack rolls for each foe, "
                    "but all attacks count as a single action in a single round. You remain limited by the amount of "
                    "Effort you can apply on one action. Anything that modifies your attack or damage applies to all "
                    "attacks. If you also have the Glaive special ability Spin Attack, you inflict 1 additional point "
                    "of damage when you use Punish All the Guilty. Action.",
            },
            '6': {"CHOICE": {
                "Damn the Guilty":
                    "(3 Intellect points) You speak words of revelation and judgment to everyone within close range, "
                    "Those whom you have designated as guilty take an additional 3 points of damage from any attack "
                    "they receive from anyone who heard your judgment. This judgment lasts for up to one minute or "
                    "until they move at least a long distance away from you. Action.",
                "Inspire the Innocent":
                    "(3 Intellect points) You speak words of encouragement and inspiration to everyone within "
                    "immediate range whom you have designated as innocent. They immediately gain a free recovery "
                    "roll. One person you choose can gain an immediate free action instead of a free recovery roll. "
                    "Justicars who have both Inspire the Innocent and the Arkus ability Inspiration gain one "
                    "additional effect when using Inspire the Innocent: the target who gains a free action also gains "
                    "an asset on it. Action.",
            }}
        },
    },
    "Moves Like A Cat": {
        "Description": "You are extremely dexterous. Your speed and agility make you almost a thing of wonder. Your "
                       "body is lithe, flexible, and graceful. Your training—or perhaps a bit of magic or "
                       "technology—allows you to move quickly and smoothly, land safely when you fall, "
                       "and avoid danger.",
        "Connection": [
            "Pick one other PC. Their occasional clumsiness and loud behavior irritate you.",
            "Pick one other PC. This character comes from the same place you do, and you knew each other as children.",
            "Pick one other PC. You aid them with advice and a helping hand when they need it. Anytime the two of you "
            "are next to each other, balancing, climbing, and jumping tasks are eased for them.",
            "Pick one other PC. They owe you a significant amount of money.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "You can take a second action this round.",
        "Minor Effect Suggestions": "You restore 2 points to your Speed Pool.",
        "Tiers": {
            '1': {
                "Reflexes": "You gain +5 to your Speed Pool. Enabler.",
                "Balance": "You are trained in balancing. Enabler.",
            },
            '2': {
                "Movement": "You are trained in climbing and jumping. Enabler.",
                "Safe Fall": "You reduce the damage from a fall by 5 points. Enabler.",
            },
            '3': {"CHOICE": {
                "Greater Reflexes": "You gain +1 to your Speed Edge. Enabler.",
                "Hard to Pin Down": "You are trained in all defense tasks. Enabler.",
            }},
            '4': {
                "Quick Strike":
                    "(4 Speed points) You make a melee attack with such speed that it is hard for your foe to defend "
                    "against, and it knocks them off balance. Your attack is eased by two steps, and the foe, "
                    "if struck, takes normal damage but is dazed so that their tasks are hindered for the next round. "
                    "Action.",
            },
            '5': {
                "Phenomenal Reflexes": "You gain an additional +5 to your Speed Pool. Enabler.",
                "Slippery": "You are trained in escaping any kind of bond or grasp. Enabler.",
            },
            '6': {"CHOICE": {
                "Burst of Action": "(6 Speed points) You can take two separate actions this round. Enabler.",
                "Deep Resources": "You gain an additional +6 to your Speed Pool. Enabler.",
            }}
        },
    },
    "Needs No Weapons": {
        "Description": "You don’t use weapons—you are a weapon. With powerful punches, kicks, and full-body moves, "
                       "you inflict incredible damage on your foes. By focusing your energy, the combined power of "
                       "your body and mind allows you to do incredible amounts of damage without depleting your "
                       "energy reserves. You might have gained your skills through intense training, various implants "
                       "and enhancements, genetic mutations, or any combination of these things. Whatever the origin "
                       "of your feats, you likely take good care of your body, ensuring that it remains the sharpest, "
                       "most dependable weapon at your disposal.",
        "Connection": [
            "Pick one other PC. They seem to believe that the only true weapons are those that you can hold in your "
            "hand, and they might look at you with disdain.",
            "Pick one other PC. This character seems incredibly unaware of their body and always happens to get in "
            "your way. If you miss your foe and accidentally hit someone else in close range, it’s likely to be them.",
            "Pick one other PC. You once trained with a close friend of theirs, and you owe that mutual friend much.",
            "Pick two other PCs. Once these two heard about your skills, they expressed interest in being your "
            "students. However, only one seems to have any aptitude.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "You strike your target in a limb, making that limb useless for the next minute.",
        "Minor Effect Suggestions": "You trip your target and knock them prone.",
        "Tiers": {
            '1': {
                "Fists of Fury": "You inflict 2 additional points of damage with unarmed attacks. Enabler.",
                "Flesh of Stone": "You have +1 to Armor if you do not wear physical armor. Enabler.",
            },
            '2': {
                "Advantage to Disadvantage":
                    "(3 Speed points) With a number of quick moves, you make an attack against an armed foe, "
                    "inflicting damage and disarming them so that their weapon is now in your hands or 10 feet (3 m) "
                    "away on the ground—your choice. This disarming attack is hindered. Action.",
                "Fighting Style": "You are trained in unarmed attacks. Enabler.",
            },
            '3': {"CHOICE": {
                "Dazing Attack":
                    "(3 Might points) You hit your foe in just the right spot, dazing them so that tasks they attempt "
                    "on their next turn are hindered. This attack inflicts normal damage. Action.",
                "Moving Like Water":
                    "(3 Speed points) You spin and move so that your defense and attacks are aided by your fluid "
                    "motion. For one minute, all your attacks and Speed defense tasks gain an asset. Enabler.",
            }},
            '4': {
                "Deflect Attacks":
                    "(4 Speed points) For one minute, you automatically deflect or dodge any ranged projectile "
                    "attacks. However, on your next turn after you’re attacked with ranged projectiles, "
                    "all your other actions are hindered. Action to initiate.",
            },
            '5': {
                "Stun Attack":
                    "(6 Speed points) You attempt a difficulty 5 Speed task to stun a creature as part of your melee "
                    "or ranged attack. If you succeed, your attack inflicts its normal damage and stuns the creature "
                    "for one round, causing it to lose its next turn. If you fail, you still make your normal attack "
                    "roll, but you don’t stun the opponent if you hit. If you have the Jack’s special ability of the "
                    "same name, these abilities cost you only 3 points instead of 6 points. Action.",
            },
            '6': {"CHOICE":{
                "Master of Style":
                    "You are specialized in unarmed attacks. If you are already specialized in unarmed attacks, "
                    "you instead deal 2 additional points of damage with unarmed attacks. Enabler.",
                "Whirling Assault":
                    "(7 Speed points) For one minute, you can attack all targets within immediate range of you. All "
                    "of the attacks have to be the same sort of attack (melee or ranged). Make a separate attack roll "
                    "for each foe. You remain limited by the amount of Effort you can apply on one action. Anything "
                    "that modifies your attack or damage applies to all of these attacks. All other actions are "
                    "hindered in any round in which you attack more than one foe using this ability. If you have the "
                    "Glaive’s Spin Attack ability, when you use it or Whirling Assault, all your attacks inflict +1 "
                    "damage. Action to initiate.",
            }}
        },
    },
    "Never Says Die": {
        "Description": "You are as stalwart, hardy, and driven as can be imagined. When others are ready to quit, "
                       "you’re just getting started.",
        "Connection": [
            "Pick one other PC. You feel the overwhelming need to impress this character, although you’re not sure "
            "why.",
            "Pick one other PC. This character seems quite capable, but in your mind, their spirit needs motivating. "
            "You’re constantly trying to convince them to keep trying, go the distance, and keep fighting the good "
            "fight.",
            "Pick one other PC. You feel very protective of this character and don’t want to see them harmed.",
            "Pick one other PC. This character comes from the same place you do, and you knew each other as children.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "Your next action is eased by two steps.",
        "Minor Effect Suggestions": "You restore 2 points to your Might Pool.",
        "Tiers": {
            '1': {
                "Rapid Recovery":
                    "Your ten-minute recovery roll takes only one action instead, so that your first two recovery "
                    "rolls are one action, the third is one hour, and the fourth is ten hours. Enabler.",
                "Push on Through":
                    "(2 Might points) You ignore the effects of terrain while moving for one hour. Enabler.",
            },
            '2': {
                "Ignore the Pain":
                    "You ignore the impaired condition and treat the debilitated condition as impaired. Enabler.",
            },
            '3': {"CHOICE":{
                "Blood Fever":
                    "When you have no points in one or two Pools, you gain an asset to attacks or defense rolls (your "
                    "choice). Enabler.",
                "Hidden Reserves":
                    "When you use an action to make a recovery roll, you also gain +1 to both your Might Edge and "
                    "your Speed Edge for ten minutes thereafter. Enabler.",
            }},
            '4': {
                "Increasing Determination":
                    "If you fail at a non-combat physical task and then retry the task (pushing open a door or "
                    "climbing a cliff, for example), the task is eased. If you fail again, you gain no special "
                    "benefits. Enabler.",
                "Outlast the Foe":
                    "If you have been in combat for five full rounds, all tasks in the remainder of that combat gain "
                    "an asset, and you deal 1 additional point of damage per attack. Enabler.",
            },
            '5': {
                "Not Dead Yet":
                    "When you would normally be dead, you instead fall unconscious for one round and then awaken. You "
                    "immediately gain 1d6 + 6 points to restore your stat Pools, and you are treated as if "
                    "debilitated (which for you is like impaired, thanks to your Ignore the Pain ability) until you "
                    "rest for ten hours. If you die again before you take your ten-hour recovery roll, you are truly "
                    "dead. If you also have the Not Dead Yet ability granted by your type, your healing from this "
                    "ability increases to 1d6 + 12. Enabler.",
            },
            '6': {"CHOICE": {
                "Final Defiance":
                    "When you would normally be dead, you instead remain conscious and active for one more round plus "
                    "one additional round each time you succeed on a difficulty 5 Might task. During these rounds, "
                    "you are debilitated (which for you is like impaired, thanks to your Ignore the Pain ability). If "
                    "you do not receive healing or otherwise gain points in a Pool during your final round(s) of "
                    "activity, you are subject to the effects of Not Dead Yet. Enabler.",
                "Ignore Affliction":
                    "(5 Might points) If you are affected by an unwanted condition or affliction (such as disease, "
                    "paralysis, mind control, broken limb, and so on, but not damage), you can ignore it and act as "
                    "if it does not affect you for one hour. If the condition would normally last less than an hour, "
                    "it is entirely negated. Action.",
            }}
        },
    },
    "Possesses a Shard of the Sun": {
        "Description": "You have the ability to create and sculpt light, to bend it away from you or gather it to use "
                       "as a weapon. Perhaps a shard of amber crystal, midnight stone, or other iotum became embedded "
                       "in your flesh and through it you can control light. Or you might have always had the gift, "
                       "a freak talent handed down to you by the ancients.",
        "Connection": [
            "Pick one other PC. You have a strong emotional connection to this character, and when in their presence, "
            "you can change the color of the light you create.",
            "Pick one other PC. They are especially perceptive to your light and occasionally your flashes leave them "
            "dazzled, hindering their defense tasks for a round.",
            "Pick one other PC. Something about their nature dampens the light. Your light-based powers cost 1 "
            "additional Intellect point if they stand immediately next to you.",
            "Pick one other PC. This character appears to have an oddity that was once yours, but that you lost in a "
            "game of chance years ago.",
        ],
        "Additional Equipment": {
            "Equipment": ["a crystal lens. When you shine light through it, the light extends for double the normal "
                          "distance."]
        },
        "Core Features": {
            "Radiant Abilities":
                "If you perform esoteries or similar abilities, those that would normally use force or other energy "
                "instead use light and heat. For example, when you use Ward, light dapples your body and flares when "
                "you would be attacked, preventing your enemies from landing a solid blow."
            ,
        },
        "Major Effect Suggestions": "An intense flash of light leaves the creature blinded for one minute.",
        "Minor Effect Suggestions": "A flash of light leaves the creature dazzled, and its defense tasks are hindered "
                                    "for one round.",
        "Tiers": {
            '1': {
                "Enlightened": "You are trained in any perception task that involves sight. Enabler.",
                "Illuminating Touch":
                    "(1 Intellect point) You touch an object, and that object sheds light to illuminate everything "
                    "in short range. The light remains until you use an action to touch the object again, or until "
                    "you’ve illuminated more objects than you have tiers, in which case the oldest objects you "
                    "illuminated go dark first. Action.",
            },
            '2': {
                "Dazzling Sunburst":
                    "(2 Intellect points) You send a barrage of dazzling colors at a creature within short range and, "
                    "if successful, inflict 2 points of damage on the target. In addition, the creature’s attacks are "
                    "hindered on its next turn, unless the target relies primarily on senses other than sight. "
                    "Action.",
            },
            '3': {"CHOICE": {
                "Burning Light":
                    "(3 Intellect points) You send a beam of light at a creature within long range and then tighten "
                    "the beam until it burns, inflicting 5 points of damage. Action.",
                "Sculpt Light":
                    "(4 Intellect points) You create an object of solid light in any shape you can imagine that is "
                    "your size or smaller that persists for about an hour. The object appears in an area adjacent to "
                    "you. The object is crude and can have no moving parts, so you can make a sword, a shield, "
                    "a short ladder, and so on. The object has the approximate mass of the real object and is level "
                    "4. Action.",
            }},
            '4': {
                "Mote of Sunlight":
                    "(4 Intellect points) A mote of light travels from you to a spot you choose within very long "
                    "range. When the mote reaches that spot, it flares and casts bright light ina radius of very long "
                    "range and darkness within 1,000 feet (300 m) of the light becomes dim light. The light lasts "
                    "until you use an action to dismiss it or you use this ability again to create a new mote. "
                    "Action.",
            },
            '5': {
                "Invisibility":
                    "(4 Intellect points) You become invisible for ten minutes. While invisible, you are specialized "
                    "in stealth and Speed defense tasks. This effect ends if you do something to reveal your presence "
                    "or position—attacking, using a special ability, moving a large object, and so on. If this "
                    "occurs, you can regain the remaining invisibility effect by taking an action to focus on hiding "
                    "your position. If you have the Nano’s ability of the same name, the effect lasts for an hour "
                    "when you use either. Action to initiate or reinitiate.",
            },
            '6': {"CHOICE":{
                "Living Light":
                    "(6+ Intellect points) Your body dissolves into a cloud of photons that instantly travel to a "
                    "location you choose and then reform. You can choose any open space big enough to contain you "
                    "that you can see within very long range, or any place you have lit by a Mote of Sunlight that is "
                    "still shining. You disappear and almost instantly reappear in the space you chose. It takes "
                    "until the end of the round for your body to become fully solid, so until the start of the next "
                    "round, you take a maximum of 1 point of damage from any given attack or source of damage. Each "
                    "level of Effort you apply allows you to bring along one additional person besides yourself, "
                    "as long as they are within immediate range when you depart. Action.",
                "Improved Sculpt Light":
                    "(7+ Intellect points) You create an object of solid light in any shape you can imagine whose "
                    "base size can fit within a 10-foot (3 m) cube. The object appears in an area adjacent to you or "
                    "floating freely in space up to a long distance away, and the object lasts for a few days. The "
                    "object is crude and can have no moving parts, so you can make a wall segment, a block, a box, "
                    "stairs, and so on. The sculpted object has the approximate mass of the real object and is level "
                    "6. If you apply Effort to increase the size of the object, each level applied increases the size "
                    "by an additional 10- foot (3 m) cube. Action.",
            }}
        },
    },
    "Radiates Vitality": {
        "Description": "You radiate a strange energy—a “biomorphic field” according to a nano you once met— that "
                       "makes you tougher than others, with an ability to heal that outstrips that of normal people. "
                       "The field seems to strengthen as you gain experience, and you’re certain that as it grows in "
                       "power, you’ll be able to touch other creatures with it to sense their presence, heal them, "
                       "detect their feelings, and possibly even hurt those who are revealed to be enemies.",
        "Connection": [
            "Pick one other PC. They were close to you in some fashion. The first time they saw you die, they grew "
            "despondent. When you returned, they were confused and upset. How they feel now, you’re not entirely sure.",
            "Pick one other PC. Your ability to regenerate doesn’t seem to work as well around them.",
            "Pick one other PC. They told you once that they worried your ability was the result of a potentially "
            "dangerous demon or alien parasite inhabiting your body. You don’t know how they feel now.",
            "Pick one other PC. You once died to save them, but they don’t know it. You may choose whether or not to "
            "tell them.",
        ],
        "Additional Equipment": {
            "Oddity": ["a small, metallic pendant that always seems to turn up, even after you’ve apparently lost it "
                       "or left it behind. It’s resisted all attempts you’ve made to scan, understand, or find out "
                       "more about it."],
        },
        "Core Features": {},
        "Major Effect Suggestions": "You spontaneously regain 2 points in two of your stat Pools.",
        "Minor Effect Suggestions": "You spontaneously regain 1 point in one of your stat Pools.",
        "Tiers": {
            '1': {
                "Mighty": "Your biomorphic field sustains you. You gain +6 to your Might Pool. Enabler.",
            },
            '2': {
                "Extra Recovery":
                    "Your biomorphic field grants you an additional one-action recovery each day. Enabler.",
            },
            '3': {"CHOICE": {
                "Detect Life":
                    "(3+ Might points) You consciously send out a pulse of your biomorphic field. You detect all "
                    "living creatures within short range, even if they are behind cover, though not if they’re behind "
                    "a force field. When you detect a creature, you detect its general location (to within an "
                    "immediate range). If you apply two additional levels of Effort, you can increase the range of "
                    "detection to long. Action.",
                "Empathy":
                    "(4 Might points) You consciously send out a pulse of your biomorphic field and focus it on a "
                    "living creature within short range that you can see or know to be there. If you succeed, "
                    "you learn that creature’s level, as well as its surface feelings and thoughts for up to the next "
                    "minute. If it becomes aware of your empathic probe, it can attempt to escape your focus with a "
                    "mental effort or by moving out of short range. Action to initiate.",
            }},
            '4': {
                "Biomorphic Healing":
                    "(4+ Might points) You consciously send out a pulse of your biomorphic field and focus it on a "
                    "living creature within short range. The target gains a free and immediate one-action recovery "
                    "roll. You can’t use this ability again on that creature until after its next ten-hour rest. "
                    "Action.",
            },
            '5': {
                "Regenerate":
                    "Your biomorphic field continues to function even if you die from violence, as long as your body "
                    "is mostly intact. One minute after your death, your biomorphic field pulses and brings you back "
                    "to life; however, you come back with a permanent 2-point deduction from your Intellect Pool. "
                    "Enabler.",
            },
            '6': {"CHOICE":{
                "Biomorphic Detonation":
                    "(7+ Might points) You radiate a pulse of biomorphic energy up to a short distance away, "
                    "but you tune it to disrupt life in an area an immediate distance across. All within the "
                    "detonation take 5 points of damage that ignores Armor (unless it is Armor provided by a force "
                    "field effect). If you apply additional Effort to increase the damage, you deal 2 additional "
                    "points of damage per level of Effort (instead of 3 points); targets in the area take 1 point of "
                    "damage even if you fail the attack roll. Action.",
                "Regenerate Other":
                    "(9 Might points) You can confer your tier 5 Regenerate ability on another creature that you "
                    "touch and attempt to return it to life, as long as its body is mostly intact. The difficulty of "
                    "the task is equal to 3 plus the number of days the target has been dead. (If the body has been "
                    "perfectly preserved in stasis or through some other non-damaging preservation mechanism, "
                    "then no time limit applies.) Enabler.",
            }}
        },
    },
    "Sees Beyond": {
        "Description": "Unlike most people, you know there are far more than three dimensions, more colors than can "
                       "be found in the rainbow, and more things in the world than most can see, sense, "
                       "or even understand. With practice and help (through drugs, lenses, manipulated energy fields, "
                       "or a combination of all three), you can perceive things that others cannot.",
        "Connection": [
            "Pick one other PC. You are fairly certain that this character doesn’t believe that your abilities are "
            "real.",
            "Pick one other PC. You see a gathering of energy and colors on this character that seem to imply they too "
            "can see beyond. Whether you ask them about it is up to you.",
            "Pick one other PC. Whenever this character is near, your abilities seem to take longer and become more "
            "difficult.",
            "Pick one other PC. Wherever this character goes, you are aware of the general distance and direction of "
            "their location.",
        ],
        "Additional Equipment": {
            "Oddity": ["a single item of your choosing—drugs, lenses, or a piece of the numenera—that helps you perceive things that others cannot. If you don’t have this item or something like it, tasks directly related to seeing beyond are hindered."]
        },
        "Core Features": {},
        "Major Effect Suggestions": "You see even more than you normally do and can ask the GM one question about "
                                    "what you’re looking at.",
        "Minor Effect Suggestions": "The period of concentration needed is cut in half.",
        "Tiers": {
            '1': {
                "See the Unseen":
                    "You can automatically perceive creatures and objects that are normally invisible, out of phase, "
                    "or only partially in this universe. When looking for things more conventionally hidden, "
                    "the task is eased. Enabler.",
            },
            '2': {
                "See Through Matter":
                    "(3+ Intellect points) You can see through matter as if it were transparent. You can see through "
                    "up to 6 inches (15 cm) of material for one round. Doing so is a task whose difficulty is equal "
                    "to the material or object’s level. In addition to the normal options for using Effort, "
                    "you can also choose to use Effort to see through another 6 inches (15 cm) of material for each "
                    "additional level of Effort you apply toward that goal. Action.",
            },
            '3': {"CHOICE": {
                "Find the Hidden":
                    "(4+ Intellect points) You see the traceries of objects as they move through space and time. You "
                    "can sense the distance and direction of any specific inanimate object that you once touched. "
                    "This takes anywhere from one action to hours of concentration, depending on what the GM feels is "
                    "appropriate due to time, distance, or other mitigating circumstances. However, you don’t know in "
                    "advance how long it will take. If you use at least two levels of Effort, once you have "
                    "established the distance and direction, you remain in contact with the object for one hour per "
                    "level of Effort used. Thus, if it moves, you are aware of its new position. Action to initiate; "
                    "action each round to concentrate.",
                "Sensor":
                    "(4 Intellect points) You create an immobile, invisible sensor within immediate range that lasts "
                    "for 28 hours. At any time during that duration, you can concentrate to see, hear, "
                    "and smell through the sensor, no matter how far you move from it. The sensor doesn’t grant you "
                    "sensory capabilities beyond the norm. If you have the Nano’s special ability of the same name "
                    "then, when you use either, you gain an asset to any perception task you attempt in conjunction "
                    "with perceiving through the sensor interface. Action to create; action to check.",
            }},
            '4': {
                "Remote Viewing":
                    "(6 Intellect points) Distance is an illusion, as all space is one space. With great "
                    "concentration, you can see another place. This ability can be used in one of two different ways: "
                    "\n* Distance and direction. Pick a spot a specific distance away and in a specific direction. "
                    "You can see from that vantage point as if you had used the Sensor ability there, but only for "
                    "one minute. \n* Think of a place that you have seen before, either conventionally or using the "
                    "other application of this power. You can see from that vantage point as if you had used the "
                    "Sensor ability there, but only for one or two rounds. \nEither application takes anywhere from "
                    "one action to hours of concentration, depending on what the GM feels is appropriate due to time, "
                    "distance, or other mitigating circumstances. However, you don’t know in advance how long it will "
                    "take. Action to initiate; action each round to concentrate.",
            },
            '5': {
                "See Through Time":
                    "(7 Intellect points) Time is an illusion, as all time is one time. With great concentration, "
                    "you can see into another time. You specify a time period regarding the place where you now "
                    "stand. Interestingly, the easiest time to view is about one hundred years in the past or future. "
                    "Viewing farther back or ahead is a nearly impossible task. This takes anywhere from one action "
                    "to hours of concentration, depending on what the GM feels is appropriate due to time, distance, "
                    "or other mitigating circumstances. However, you don’t know in advance how long it will take. "
                    "Action to initiate; action each round to concentrate.",
            },
            '6': {"CHOICE": {
                "Mental Projection":
                     "(6+ Intellect points) Your mind fully leaves your body and manifests anywhere you choose within "
                     "immediate range. Your projected mind can remain apart from your body for up to 28 hours. This "
                     "effect ends early if your Intellect Pool is reduced to 0 or if your projection touches your "
                     "resting body. Your disembodied mind is a psychic construct that looks like you, though its "
                     "frayed edges trail off into nothingness. You control this body as if it were your normal body "
                     "and can act and move as you normally would with a few exceptions. You can move through solid "
                     "objects as if you were phased, and you ignore any terrain feature that would impede your "
                     "movement. Your attacks inflict 3 fewer points of damage (to a minimum of 1) and you take 3 "
                     "fewer points of damage (to a minimum of 1) from physical sources, unless they can affect "
                     "transdimensional or phased beings, in which case you take full damage. Regardless of the "
                     "source, you take all damage as Intellect damage first. Your mind can travel up to 1 mile (1.5 "
                     "km) from your body. Each level of additional Effort applied extends the range that you can "
                     "travel by 1 mile (1.5 km). Your physical body is helpless until this effect ends. You cannot "
                     "use your physical senses to perceive anything. For example, your body could sustain a "
                     "significant injury, and you wouldn’t know it. Your body cannot take Intellect damage, "
                     "so if your body takes enough damage to reduce both your Might Pool and your Speed Pool to 0, "
                     "your mind snaps back to your body, and you are stunned until the end of the next round as you "
                     "try to reorient yourself to your predicament. Action to initiate.",
                "Total Awareness":
                    "You possess such a high level of awareness that it’s very difficult to surprise, hide, or sneak "
                    "up on you. When you apply a level of Effort to initiative and perception tasks, you gain two "
                    "free levels of Effort. Enabler.",
            }}
        },
    },
    "Shepherds the Community": {
        "Description": "You have an abiding affection for the community you live in, have adopted, or guard from "
                       "afar. It’s not just the place, but also the people you want to keep safe and healthy and see "
                       "have success in their life. Certainly, there are individuals within the community who are "
                       "more troublesome than others, but unless they become an actual danger to the others, "
                       "you include them in those you shepherd. To accomplish your goal, you’ve honed not only your "
                       "ability to fight in order to preserve the community against invaders, but also your ability "
                       "to understand the concerns of the community and persuade them toward smart decisions about "
                       "the problems that face them now or could crop up later if not guarded against.",
        "Connection": [
            "Pick one other PC. This character grew up in the community you shepherd, and you are especially keen to "
            "see that they stay safe when they venture beyond it.",
            "Pick one other PC. You originally thought they might be a danger to the community, which is why you "
            "introduced yourself, in order to discover if your first impression was correct.",
            "Pick one other PC. This character is from a community that has been a rival of the community you protect, "
            "but you hope that maybe through them, you can build a bridge.",
            "Pick one other PC. You hope this character will come to find as much comfort in your community as you.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "Your foe is terrified by your dedication and flees.",
        "Minor Effect Suggestions": "Your foe is so intimidated by your dedication that it backs away, unwilling to "
                                    "attack on its next turn. It can still defend itself.",
        "Tiers": {
            '1': {
                "Community Knowledge":
                    "(2 Intellect points) If you’ve invested yourself in a community and have spent at least a few "
                    "months living there, you can learn things about it through a variety of methods. Sometimes "
                    "contacts slip the information to you. Other times, you’re able to draw conclusions simply by "
                    "what you can see and hear. When you use this ability, you can ask the GM one question about the "
                    "community and get a very short answer. Action.",
                "Community Activist":
                    "When speaking to others in the community you foster, you are trained in persuasion and "
                    "intimidation tasks about topics that directly relate to the community. Enabler.",
            },
            '2': {
                "Community Protector":
                    "Choose one type of attack in which you are not already trained: light bashing, light bladed, "
                    "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, "
                    "or heavy ranged. You are trained in attacks using that type of weapon. Enabler. ",
            },
            '3': {"CHOICE": {
                "Community Advocate":
                    "While you are present within the community, and actively and personally working on behalf of the "
                    "community, its effective rank for all tasks, except for attacks and defense, is +1 (this "
                    "includes determining health and infrastructure values, but not damage inflicted). If you also "
                    "have the Arkus Community Leader ability, the +1 rank modifier also includes attacks and defense. "
                    "Enabler.",
                "Shepherd’s Fury":
                    "You inflict 3 additional points of damage when engaging in combat that directly relates to "
                    "advancing the needs of a community you foster. (You and the GM can decide whether a particular "
                    "situation warrants the additional damage.) Enabler.",
            }},
            '4': {
                "Inexhaustible Shepherd":
                    "You cannot shepherd a community without immense stamina. You gain +3 to your Might Pool and +3 "
                    "to your Intellect Pool. Enabler.",
            },
            '5': {
                "Unassailable":
                    "Your devotion to keeping your community safe against all dangers has hardened you against all "
                    "vicissitudes. You are trained in defense tasks. Enabler.",
            },
            '6': {"CHOICE": {
                "Master Combatant":
                    "Choose one type of attack in which you are already trained: light bashing, light bladed, "
                    "light ranged, medium bashing, medium bladed, medium ranged, heavy bashing, heavy bladed, "
                    "or heavy ranged. You are specialized in attacks using that type of weapon. Enabler.",
                "Protective Wall":
                    "(6+ Might points) When engaging in combat that directly relates to defending a community you are "
                    "fostering, you can attack up to five different foes as a single action as long as they are all "
                    "within immediate range. If you hit an attacker, they are pushed back an immediate distance. All "
                    "of the attacks have to be the same sort of attack (melee or ranged). Make a separate attack roll "
                    "for each foe. You remain limited by the amount of Effort you can apply on one action. Anything "
                    "that modifies your attack or damage applies to all of these attacks. In addition to the normal "
                    "options for using Effort, you can also choose to use Effort to increase the number of foes you "
                    "can attack with this ability, one additional foe per level of Effort. Enabler.",
            }}
        },
    },
    "Shreds the Walls of the World": {
        "Description": "When you move, your body changes state and becomes partially phased, reflecting a bizarre "
                       "alternate dimension where distance and time are different than they are in the Ninth World. "
                       "It’s only when you’re still that you remain solid and fully part of the real world. Sometimes "
                       "that’s a relief, but other times you feel like you’re stuck in wet sand. Moving is your key "
                       "to changing phase—and perhaps happiness. While you’re phased, you skate along the surface of "
                       "reality far more quickly than others. Such rapid movement across normal reality sometimes "
                       "leaves behind scratches, which you can selectively make, suppress, or bear down upon to "
                       "create particularly devastating attacks and, eventually, phase detonations.",
        "Connection": [
            "Pick one other PC. For some reason, they never lose a sense of where you are, no matter how you sprint "
            "around, change phase, or even become invisible (to everyone else).",
            "Pick one other PC. You recently discovered that if they stand near you when you begin a Phase Sprint, "
            "they become partially phased in the same way as you for one round, though they can’t sprint or use any "
            "other abilities of this focus.",
            "Pick one other PC. Seeing you phase seems to trigger some unpleasant memory in this character. That "
            "memory is up to the other PC, although they may not be able to consciously recall what the memory might "
            "be.",
            "Pick one other PC. Something about them interferes with your abilities. When they stand next to you, your "
            "focus abilities cost 1 additional point.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "The target is stunned and loses their next action.",
        "Minor Effect Suggestions": "The target is dazed, and their next action is hindered.",
        "Tiers": {
            '1': {
                "Phase Sprint":
                    "(1+ Speed points) You can run up to a long distance as long as you take no other actions. During "
                    "your action and until the beginning of your next turn, you are partially phased, "
                    "and some attacks pass through you harmlessly. While phased, you gain an asset to your Speed "
                    "defense tasks, but you lose any benefit from armor you wear. Note that some of your other "
                    "special abilities enable specific actions that you can take while using Phase Sprint. For "
                    "instance, when using Disrupting Touch, you can make one touch attack while moving (though this "
                    "ends your movement). Action.",
                "Disrupting Touch":
                    "(1+ Might points) You can turn your Phase Sprint into a melee attack by purposefully grazing "
                    "another creature as you run. When you do, the touch releases a violent blast of energy that "
                    "inflicts 2 points of damage to the target (ignores Armor). Whether you hit or miss, "
                    "your movement (and turn) ends immediately, which puts you within immediate distance of your "
                    "target. If you apply Effort to increase damage rather than to ease the task, you deal 2 "
                    "additional points of damage per level of Effort (instead of 3 points); the target takes 1 point "
                    "of damage even if you fail the attack roll. Enabler.",
            },
            '2': {
                "Scratch Existence":
                    "(1+ Might points) You can choose to phase in a way that “scratches” normal matter in a long "
                    "streak as you run using Phase Sprint. This tears a bit at you, too, reflected by the Might cost. "
                    "When you use Phase Sprint, you inflict 2 points of damage (ignores Armor) to one target you "
                    "select as you pass within immediate range, without triggering Disrupting Touch. In addition to "
                    "the normal options for using Effort, you can also choose to use Effort to increase the number of "
                    "targets along your path that you can attack as part of the same action. Make a separate attack "
                    "roll for each foe. You remain limited by the amount of Effort you can apply on one action. "
                    "Anything that modifies your attack or damage applies to all of these attacks. Alternatively, "
                    "if you apply Effort to increase the damage rather than ease the task, you deal 2 additional "
                    "points of damage per level of Effort (instead of 3 points); the target takes 1 point of damage "
                    "even if you fail the attack roll. Enabler.",
            },
            '3': {"CHOICE":{
                "Invisible Phasing":
                    "(4 Might points) You become invisible while Phase Sprinting and during the following round. "
                    "While invisible, stealth and Speed defense tasks are eased by two steps (replacing the asset to "
                    "Speed defense tasks provided by Phase Sprint). The first attack you make using any Shreds the "
                    "Walls of the World attack abilities is also eased by two steps; however, if you attack a "
                    "creature, Invisible Phasing ends immediately instead of lasting for one additional round. If you "
                    "have the Nano Invisibility esotery, you can remain invisible during the entire round, "
                    "which means that if you use Scratch Existence or Shred Existence, attacking each target along "
                    "your path is eased by two steps. Enabler.",
                "Walk Through Walls":
                    "(2 Intellect points) You can slowly pass through physical barriers at a rate of 1 inch (2.5 cm) "
                    "per round (minimum of one round to pass through any barrier). You can’t act (other than moving) "
                    "or perceive anything until you pass entirely through the barrier. You can’t pass through energy "
                    "barriers. Action.",
            }},
            '4': {
                "Phase Detonation":
                    "(2+ Might points) When you use Phase Sprint or Walk Through Walls, you can choose to "
                    "significantly damage normal matter around you with a blast of transdimensional energy when you "
                    "first go into or come out of phase (your choice). This detonation inflicts 4 points of damage "
                    "that ignores Armor to all creatures and objects within immediate range. If you apply Effort to "
                    "increase the damage rather than ease the task, you deal 2 additional points of damage per level "
                    "of Effort (instead of 3 points); targets in the area take 1 point of damage even if you fail the "
                    "attack roll. Enabler.",
            },
            '5': {
                "Very Long Sprinting":
                    "When you use Phase Sprint, you can travel up to a very long distance as your action instead of a "
                    "long distance. Enabler.",
            },
            '6': {"CHOICE":{
                "Shred Existence":
                    "When you use Disrupting Touch, Scratch Existence, or Phase Detonation, you inflict an additional "
                    "5 points of damage that ignores Armor. Enabler.",
                "Untouchable While Moving":
                    "(4 Intellect points) You change your phase state for the next minute so that you can’t affect or "
                    "be affected by normal matter or energy, as long as you move at least an immediate distance each "
                    "round while phased. If you don’t move on your turn, the effect ends. While you are phased, "
                    "only mental attacks and special transdimensional energies, devices, or abilities can affect you, "
                    "but likewise you can’t attack, touch, or otherwise affect anything. Action to initiate.",
            }}
        },
    },
    "Thunders": {
        "Description": "For you, sound is a tapestry of sensation that surpasses light and perhaps even vision "
                       "itself. Existence is a soundscape of noise whose meanings are not only clear, but insistent. "
                       "You can’t ignore them. Then again, why would you want to? You’ve learned how to manipulate "
                       "sound by emitting both constructive and destructive interference. At first, "
                       "your manipulations of the soundscape are brutal and straightforward, but the more you learn, "
                       "the more you know that subtleties of sound manipulation will not be beyond you for long. Even "
                       "so, you’ll exult the most when you allow your abilities to thunder.",
        "Connection": [
            "Pick one other PC. You can always hear this character, even when the sound of your abilities seems to "
            "drown everyone else out.",
            "Pick one other PC. You suspect that this character is slightly deaf, because they don’t seem to react to "
            "your abilities like most others do.",
            "Pick one other PC. You once paid off a large debt for this character. Whether they’re grateful is up to "
            "them, and whether you think you’re owed a debt in return is up to you.",
            "Pick two other PCs. They both have perfect pitch, which impresses you greatly.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "The sound deafens the target for about a minute, during which time it is dazed.",
        "Minor Effect Suggestions": "The sound knocks the target to the ground.",
        "Tiers": {
            '1': {
                "Thunder Beam":
                    "(2 Might points) You direct a beam of focused sound at a target within long range, inflicting 2 "
                    "points of damage and inducing a resonant destructive wave in their body. Each round after this "
                    "initial attack, you can make another roll for the destructive wave to inflict an additional 1 "
                    "point of damage to the target. If you fail this roll, the destructive wave ends. Unlike the "
                    "initial attack, the destructive wave ignores Armor. \nAlternatively, you can set up a destructive "
                    "resonance in a physical melee weapon for one minute or until you let go of it. All attacks made "
                    "with the target weapon inflict 1 additional point of damage. Action to initiate.",
            },
            '2': {
                "Sound Conversion Barrier":
                    "Attacks that hit you—especially energy attacks like focused light, heat, radiation, "
                    "and transdimensional energy—are partially converted to surges of harmless noise similar to the "
                    "sound of a wave crashing to shore. This ability grants you +1 Armor against all attacks and an "
                    "additional +2 Armor against energy attacks. Enabler.",
            },
            '3': {
                "CHOICE":{
                     "Echolocation":
                         "You are especially sensitive to sound and vibration, so much so that you can sense your "
                         "environment within a short distance regardless of your ability to see. Enabler.",
                    "Nullify Sound":
                        "(3 Might points) You pulse perfectly misaligned sounds within short range to create a zone "
                        "of absolute quiet up to an immediate distance across for one minute. All sound is canceled "
                        "in the zone. Action to initiate.",
                },
            },
            '4': {
                "Shattering Shout":
                    "(5 Might points) Your focused shout sets up a destructive resonance in a creature or object "
                    "within long range. Nothing happens on the round you strike your target other than an ominous "
                    "humming or buzzing sound emitted by the target. But on your next turn, the resonance shatters "
                    "discrete inanimate objects, inflicts major damage to structures and installations, or inflicts 4 "
                    "points of damage on a creature (ignores Armor). \nIf you shatter a discrete object, it shatters "
                    "explosively, inflicting 1 point of damage on all creatures and objects within immediate range of "
                    "it. If you apply Effort to increase the damage rather than ease the task, you deal 2 additional "
                    "points of damage per level of Effort (instead of 3 points); targets in the area take 1 point of "
                    "damage even if you fail the attack roll. Action to initiate.",
            },
            '5': {
                "Subsonic Rumble":
                    "(2 Intellect points) For one minute or until you use your ability to manipulate sound in some "
                    "other way, you emit a subsonic rumble that most living creatures can’t hear but which has an "
                    "effect on them all the same. The effect lasts for one minute and affects all creatures you "
                    "select within short range. All tasks related to resisting persuasion, intimidation, and fear are "
                    "hindered by two steps for affected targets. Action to initiate.",
                "Amplify Sounds":
                    "(2 Might points) For one minute, you can amplify distant or small sounds so that you can hear "
                    "them clearly, even if it’s a conversation or the sound of a small animal moving through an "
                    "underground burrow up to a very long distance away. You can attempt to perceive the sound even "
                    "if interceding barriers block it or if the sound is very slight, though this requires a few "
                    "additional rounds of concentration. To discriminate the sound you wish in a noisy environment "
                    "might also require a few additional rounds of concentration as you audibly explore the "
                    "surrounding soundscape. Given enough time, you could pinpoint every conversation, "
                    "every breathing creature, and every device creating noise within range. Action to initiate, "
                    "up to several rounds to complete, depending on the difficulty of the task.",
            },
            '6': {"CHOICE": {
                "Earthquake":
                    "(7 Might points) You direct your destructive resonance into the ground and trigger an earthquake "
                    "centered on a spot you can see within very long range. The ground within short range of that "
                    "spot heaves and shakes for five minutes, causing damage to structures and terrain in the area. "
                    "Buildings and terrain features shed debris and rubble. Each round, creatures in the area take "
                    "either 3 points of damage due to the general shaking, or 6 points of damage if in or adjacent to "
                    "a structure or terrain feature shedding debris. Action to initiate.",
                "Lethal Vibration":
                    "(7 Might points) You set up a lethal vibration in your own body and pass it to a creature you "
                    "touch with a successful attack. If the target is level 2 or lower, it explodes in a peal of "
                    "thunder. If the target is level 3 or higher, it sustains 6 points of damage and is stunned on "
                    "its next action. If the target is a PC of any tier, they move down one step on the damage track. "
                    "In addition to the normal options for using Effort, you can choose to use Effort to affect a "
                    "more powerful target (one level of Effort means a target of up to level 3 explodes and a target "
                    "of level 4 or higher takes damage and is stunned, and so on). Action.",
            }}
        },
    },
    "Touches the Sky": {
        "Description": "The storm smells like life to you—like love. Electricity charges the air, dances across your "
                       "skin, and connects you to the wind, the weather, and the sky. That connection is due to a "
                       "device fused to your flesh, a mutation, or just your training with the nanomachines that "
                       "suffuse everything. You issue commands through that connection, and the weather listens. The "
                       "winds curl to your desire; they lift you, protect you, and give you the power to summon "
                       "storms or break them apart. An electrical storm, a blizzard, or—when your mastery reaches its "
                       "zenith—even a tornado is something you can call up and loose upon the world.",
        "Connection": [
            "Pick one other PC. You can’t affect this character with your focus abilities, though you don’t know why.",
            "Pick one other PC. You recently discovered that if they stand near you when you use your tier 1 Hover "
            "ability, they too lift into the air. They must remain within short range of you to retain the effect, "
            "and it lasts only for as long as you hover yourself.",
            "Pick one other PC. Their parents (or other loved ones) were killed in a freak storm. When they "
            "discovered your connection to the weather, they didn’t know how to react. They either feel anger toward "
            "you or hope you can help provide some answers; it’s up to them.",
            "Pick one other PC. Something about them interferes with your abilities. When they stand near you, your "
            "focus abilities cost 1 additional point.",
        ],
        "Additional Equipment": {
            "Oddities": ["a device that sometimes crackles with electricity. Whoever holds it is immune to your "
                         "weather abilities (but only if you willingly give it to them)"]
        },
        "Core Features": {
            "Weather Abilities":
                "If you wield powers that would normally use force or other energy, they instead use various effects "
                "generated by extreme weather. For example, a blast of energy could be a wind blast, a blast of "
                "blizzard cold, or a small bolt of lightning. Also, if you wish, you can swap an ability gained from "
                "your type for the following. \nZap (2 Intellect points). You attack a foe within short range with an "
                "electrical discharge that inflicts 4 points of damage and dazes your target so that its next action "
                "is hindered. Action.",
        },
        "Major Effect Suggestions": "The target is dazed, and their next action is hindered.",
        "Minor Effect Suggestions": "The target is stunned and loses their next action.",
        "Tiers": {
            '1': {
                "Hover":
                    "(1 Intellect point) You float slowly into the air. As your action, you can concentrate to remain "
                    "motionless in the air or float up to a short distance, but no more; otherwise, you drift with "
                    "the wind or with any momentum you have gained. This effect lasts for up to ten minutes. If you "
                    "also have the Hover ability granted by your type, you can hover for twenty minutes and move your "
                    "normal speed. Action to initiate.",
            },
            '2': {
                "Wind Armor":
                    "(1 Intellect point) When you wish it, a cyclone of wind surrounds your body for ten minutes, "
                    "giving you +1 to Armor and an additional +2 to Armor against physical projectile weapons "
                    "specifically. While the cyclone is active, you feel no discomfort from the wind, and you can "
                    "interact with other creatures and objects normally because the wind flow automatically diverts "
                    "to enable such interaction. Enabler.",
            },
            '3': {"CHOICE":{
                "Lightning Discharge":
                    "(5+ Intellect points) You blast a fan of lightning out to short range in an arc that is "
                    "approximately 50 feet (15 m) wide at the end. This discharge inflicts 4 points of damage. If you "
                    "apply Effort to increase the damage rather than to decrease the difficulty, you deal 2 "
                    "additional points of damage per level of Effort (instead of 3 points); targets in the area take "
                    "1 point of damage even if you fail the attack roll. Action.",
                "Storm Seed":
                    "(3 Intellect points) If outside or in a large-enough enclosed space, you can seed a natural "
                    "storm of a kind common to the area. Doing so requires at least an hour’s concentration as you "
                    "use your connection to nanites in the air to initiate proper conditions, though it could take "
                    "longer if the GM feels there are additional obstacles at play. Once the storm begins, "
                    "it lasts for about ten minutes. Once during that period, you can create a more dramatic and "
                    "specific effect appropriate to that kind of storm, such as a lightning strike, a squall of giant "
                    "hailstones, the brief touchdown of a twister, a single gust of hurricane-force winds, "
                    "and so on. These effects must occur within long range of your location. You must spend your turn "
                    "concentrating to create the effect, which occurs a round later. The effect inflicts 6 points of "
                    "damage, after which the storm begins to disperse. Action to initiate, an hour or more to "
                    "complete.",
            }},
            '4': {
                "Windrider":
                    "(4+ Intellect points) You summon winds that pick you up and allow you to fly for one minute at a "
                    "rate of up to a long distance each round. For each level of Effort you apply, you can carry one "
                    "ally of about your size with you through the air or increase the duration of the effect by one "
                    "minute. Action to initiate.",
            },
            '5': {
                "Cold Burst":
                    "(5+ Intellect points) You emit a blast of cold in all directions up to short range. All within "
                    "the burst take 3 points of damage and are dazed on their next turn, hindering any actions they "
                    "attempt. If you apply Effort to increase the damage rather than to decrease the difficulty, "
                    "you deal 2 additional points of damage per level of Effort (instead of 3 points), and targets in "
                    "the area take 1 point of damage even if you fail the attack roll. Action.",
            },
            '6': {"CHOICE":{
                "Control Weather":
                    "(10 Intellect points) You change the weather in your general region. If performed indoors, "
                    "this creates minor effects, such as mist, mild temperature changes, and so on. If performed "
                    "outside, you can create rain, fog, snow, wind, or any other kind of normal (not overly severe) "
                    "weather. The change lasts for a natural length of time so that a storm might last for an hour, "
                    "fog for two or three hours, and snow for a few hours (or for ten minutes if it’s out of season). "
                    "For the first ten minutes after activating this ability, you can create more dramatic and "
                    "specific effects, such as lightning strikes, giant hailstones, twisters, hurricane-force winds, "
                    "and so on. These effects must occur within 1,000 feet (300 m) of your location. You must spend "
                    "your turn concentrating to create an effect or maintain it in a new round. These effects inflict "
                    "6 points of damage each round. If you have the Nano ability of the same name, the cost for the "
                    "ability is 7 Intellect points instead of 10. Action to initiate.",
                "Wind Chariot":
                    "(7+ Intellect points) You summon winds that pick you up and allow you to fly for up to a long "
                    "distance each round in combat or with an overland speed of up to 200 miles per hour (320 kph) "
                    "for up to ten hours. For each level of Effort you apply, you can bring one ally of about your "
                    "size with you through the air or increase the duration of the effect by one hour. Action to "
                    "initiate.",
            }}
        },
    },
    "Wields Words Like Weapons": {
        "Description": "You are a talker. Maybe you got your start telling stories, arguing with your siblings, "
                       "running a shop, and so on. You learned how people think, how they respond to some lines of "
                       "argument and words more than others, and how to apply that influence selectively. You "
                       "negotiate for your sake, on behalf of others, or for a cause you believe in. Charismatic, "
                       "your natural talent shows through any time you open your mouth to speak. You know when it’s "
                       "appropriate to joke, when to be serious, and, sometimes, when an insult is required to wound "
                       "someone’s pride in just the right way to get what you want.",
        "Connection": [
            "Pick one other PC. This character tends to believe everything you say, even when you are clearly joking. "
            "It’s up to you whether you want to tone down your rhetoric when speaking to them.",
            "Pick one other PC. You convinced them not to break up with their significant other, thinking you were "
            "helping. Now the relationship seems even more terrible, and you regret your earlier action.",
            "Pick one other PC. They’ve always been there for you and helped you when you couldn’t help yourself.",
            "Pick one other PC. You both had a mutual friend who died. You’re not sure whether this character blames "
            "you or not.",
        ],
        "Additional Equipment": {},
        "Core Features": {},
        "Major Effect Suggestions": "The target is favorably disposed toward you for days or more.",
        "Minor Effect Suggestions": "The target is dazed for a round, hindering all tasks they attempt on their next "
                                    "turn.",
        "Tiers": {
            '1': {
                "How Others Think":
                    "You have a sense of how people think. You’re trained in one of the following tasks: persuasion, "
                    "deception, or detecting falsehoods. Enabler.",
                "Misdirect Blame":
                    "(2+ Intellect points) Using your clever words and knowledge of others, you can attempt to alter "
                    "the narrative so that a target of up to level 3 within short range becomes uncertain of its "
                    "conviction in one simple area, such as their conviction that you just stole a fruit from their "
                    "stand or their belief that they’ve never met you before. This effect usually lasts only for the "
                    "period of time you spend speaking, and perhaps up to a minute longer, before the target realizes "
                    "its error. In addition to the normal options for using Effort, you can also choose to use Effort "
                    "to increase the target level that can be affected. Afterward, all your tasks to persuade or "
                    "otherwise socially interact with the target are hindered. Action.",
            },
            '2': {
                "Negotiate":
                    "(3 Intellect points) In any gathering where two or more people are trying to establish the truth "
                    "or come to a decision, you can sway the verdict with masterful rhetoric. If you are given a few "
                    "rounds or more to argue your point, either the decision goes your way or, if someone else "
                    "effectively argues a competing point, any associated persuasion or deception task is eased by "
                    "two steps. Action to initiate, one or more rounds to complete.",
            },
            '3': {"CHOICE":{
                "Command":
                    "(3 Intellect points) Through sheer force of will and charisma, you issue a simple command to a "
                    "single living creature, which attempts to carry out your command as its next action. The "
                    "creature must be within short range and be able to understand you. The command can’t inflict "
                    "direct harm on the creature or its allies, so “Commit suicide” won’t work, but “Flee” might. In "
                    "addition, the command can require the creature to take only one action, so “Open the door” might "
                    "work, but “Open the door and run through it” won’t. A commanded creature can still defend itself "
                    "normally and return an attack if one is made on it. If you possess a type ability that allows "
                    "you to command a creature, you can target two creatures at once as your base effect if you use "
                    "either ability. Action.",
                "Keen Mind": "You gain +1 to your Intellect Edge. Enabler.",
            }},
            '4': {
                "Interruption":
                    "(4 Intellect points) Your vociferous, booming command prevents a creature within short range "
                    "from taking any action for one round. It can defend itself if attacked, but when it does so, "
                    "its defense is hindered by two steps. Each additional time you attempt this ability against the "
                    "same target, you must apply one more level of Effort than you applied on the previous attempt. "
                    "Action.",
            },
            '5': {
                "Community Negotiator":
                    "You are trained in two of the following skills: persuasion, deception, intimidation, research, "
                    "knowledge in one area, or seeing through deception. If you choose a skill in which you’re "
                    "already trained, you become specialized in that skill instead. In addition, an allied "
                    "community’s effective rank is increased by 1 for tasks related to the skills you choose, "
                    "as long as you have been active and working on the community’s behalf in any given seven-day "
                    "period. Enabler.",
            },
            '6': {"CHOICE":{
                "Break Their Mind":
                    "(7+ Intellect points) Using your clever words and knowledge of others, and given a couple of "
                    "rounds of conversation to gain a few specific pieces of context regarding your target, "
                    "you can utter a sentence designed to cause your target immediate psychological distress. If the "
                    "target can hear you, it suffers 6 points of Intellect damage (ignores Armor) and forgets the "
                    "last day of its life, which might mean it forgets you and how it came to be where it currently "
                    "is. In addition to the normal options for using Effort, you can also choose to use Effort to "
                    "attempt to break the mind of one additional target who can hear you. Action to initiate, "
                    "action to complete.",
                "Explains the Ineffable":
                    "Through anecdotes, historical retellings, and citing knowledge that few but you have previously "
                    "understood, you enlighten your friends. After spending 28 hours with you, once per day, "
                    "each of your friends can ease a particular task by two steps. This benefit is ongoing while you "
                    "remain in your friends’ company. It ends if you leave, but it resumes if you return to your "
                    "friends’ company within 28 hours. If you leave your friends’ company for longer than that, "
                    "you must spend another 28 hours together to reactivate the benefit. Enabler.",
            }}
        },
    }
}

foci = dict(discovery_foci, **destiny_foci)

major_effects = ["Disarm", "Knock Down", "Stun"]

weapon_damages = {"LIGHT": 2, "MEDIUM": 4, "HEAVY": 6}

object_damage_track = ["Intact", "Minor Damage", "Major Damage", "Destroyed"]

long_term_benefits = ["Contact", "Home", "Title or Job", "Wealth", "Artifact"]  # 3xp
