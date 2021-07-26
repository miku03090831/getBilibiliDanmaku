-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vtuber
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate` (
  `rate` varchar(255) DEFAULT NULL,
  `vtuber_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate`
--

LOCK TABLES `rate` WRITE;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
INSERT INTO `rate` VALUES ('0','3295'),('0','38829'),('0.0007374631268436405','45502'),('0','52522'),('0','70070'),('0.3848341232227488','72960'),('0.07869481765834929','117906'),('0.3475103734439834','130209'),('0.3514018691588785','140378'),('0.07594936708860756','163653'),('0.17099056603773588','186463'),('0.16675461741424802','198297'),('0.05517241379310345','249243'),('0.20915032679738566','257319'),('0.23500810372771475','264161'),('0.3437710437710437','282994'),('0.5568942436412316','298484'),('0.20100502512562812','314993'),('0.4516806722689075','317000'),('0.1026785714285714','352332'),('0.2369020501138952','370515'),('0.09695290858725758','408696'),('0.26','433307'),('0.07526881720430112','451793'),('0.16710457172884918','477792'),('0.14175654853620956','487902'),('0.12105263157894741','492862'),('0.14237288135593218','501280'),('0.3624925104853205','510047'),('0.39538043478260865','512480'),('0.1424418604651163','518817'),('0.04761904761904767','529249'),('0.08060453400503775','545511'),('0.3564593301435407','607286'),('0.32482598607888635','610390'),('0.25149700598802394','611813'),('0.2862049227246709','620903'),('0.08837209302325577','625978'),('0.2849389416553596','632960'),('0.10643015521064303','640283'),('0.16731517509727623','651649'),('0.16400911161731202','659401'),('0.06849315068493156','679945'),('0.12638580931263854','720964'),('0.15839243498817968','731556'),('0.17268041237113407','738406'),('0.09839357429718876','741520'),('0.1157407407407407','743603'),('0.26308539944903586','744713'),('0.156060606060606','745493'),('0.06217616580310881','749499'),('0.24102564102564106','839059'),('0.17344753747323338','846180'),('0.09523809523809523','871336'),('0.12064343163538871','899804'),('0.07321428571428568','922573'),('0.07096774193548383','1329434'),('0.0915178571428571','1352646'),('0.10108303249097472','1359996'),('0.03319502074688796','1382784'),('0.22696629213483144','1401928'),('0.4094827586206896','1420223'),('0.2962962962962963','1442771'),('0.18872017353579174','1473830'),('0.24020887728459528','1480838'),('0.13609467455621305','1485569'),('0.3804780876494024','1506609'),('0.16704805491990848','1516482'),('0.05833333333333335','1523623'),('0.034267912772585674','1590297'),('0.1338028169014085','1610379'),('0.15183723048891584','1612112'),('0.21995926680244404','1697694'),('0.13521126760563384','1721774'),('0.12268518518518523','1740548'),('0.14598540145985406','1750561'),('0.056367432150313146','1764912'),('0.13054830287206265','1780645'),('0.09708737864077666','1791514'),('0.17226890756302526','1817276'),('0.17113402061855665','1836495'),('0.09722222222222221','1869304'),('0.18144450968878445','1950658'),('0.22822417285617824','2100679'),('0.11491442542787289','2128310'),('0.08227848101265822','2141017'),('0.15642458100558654','2239559'),('0.057366362451108266','2299184'),('0.12605042016806722','2308730'),('0.16582914572864327','2341174'),('0.16000000000000003','2683466'),('0.24943820224719104','2878144'),('0.22153209109730854','3009298'),('0.08238636363636365','3032688'),('0.23202614379084963','3034238'),('0.18562874251497008','3035105'),('0.37327499158532484','3046429'),('0.1808885754583921','3149619'),('0.23560209424083767','3303103'),('0.112540192926045','3328498'),('0.0853825136612022','3821157'),('0.11250000000000004','3934727'),('0.33333333333333337','3985676'),('0.23866348448687347','4071581'),('0.13961038961038963','4098782'),('0.5429042904290429','4176573'),('0.08444444444444443','4365283'),('0.23715415019762842','4690327'),('0.07861635220125784','4711217'),('0.0911764705882353','4718716'),('0.17892644135188862','4832930'),('0.11764705882352944','4882872'),('0.07657657657657657','4911722'),('0.3761301989150091','5005968'),('0.2376395534290271','5563350'),('0.31930960086299887','5659864'),('0.17431906614785997','6055289'),('0.13617021276595742','6223905'),('0.22413793103448276','6268594'),('0.2802850356294537','6483727'),('0.24461839530332685','6747203'),('0.06687898089171973','7340453'),('0.24936386768447838','7410885'),('0.05895691609977327','7591465'),('0.10126582278481011','7684135'),('0.21111111111111114','7706705'),('0.0959147424511545','8041302'),('0.10850801479654748','8119834'),('0.10909090909090913','8170242'),('0.1634146341463415','8363141'),('0.2680412371134021','8760033'),('0.08457249070631967','8881297'),('0.25072674418604646','9066351'),('0.19648093841642233','9361427'),('0.10144927536231885','9561918'),('0.13943355119825707','9736638'),('0.07586206896551728','10030059'),('0.052238805970149294','10759587'),('0.13650793650793647','10880609'),('0.13802816901408455','11137181'),('0.4420368364030336','11253297'),('0.24395161290322576','11431931'),('0.27380952380952384','11707013'),('0.20999999999999996','12120515'),('0.13793103448275867','12450452'),('0.13095238095238093','12497617'),('0.19999999999999996','12945093'),('0.0714285714285714','13043029'),('0.05714285714285716','13630808'),('0.049907578558225474','13908542'),('0.08205128205128209','14350494'),('0.16453201970443354','14387072'),('0.07990314769975781','14405936'),('0.17948717948717952','15551343'),('0.1428571428571429','15641218'),('0.1822784810126582','17479767'),('0.39051918735891644','17492464'),('0.05054151624548742','17511965'),('0.08096280087527352','17661166'),('0.24739583333333337','17794913'),('0.1975580464371497','18149131'),('0.11555555555555552','20272422'),('0.120253164556962','20699734'),('0.21395348837209305','20873473'),('0.15652173913043477','21151384'),('0.17159763313609466','21203842'),('0.2183908045977011','21374533'),('0.11374407582938384','21685335'),('0.1313559322033898','21693393'),('0.058666666666666645','23155481'),('0.08018867924528306','23279074'),('0.08268733850129195','26087398'),('0.05555555555555558','26398020'),('0.4390243902439024','26541399'),('0.10752688172043012','27322128'),('0.09302325581395354','27554691'),('0.3310344827586207','27564630'),('0.09615384615384615','32365653'),('0.15736040609137059','32906095'),('0.04869565217391303','33419912'),('0.125','33801277'),('0.09523809523809523','34237849'),('0.20945945945945943','34423885'),('0.09745762711864403','35231887'),('0.22435897435897434','35819875'),('0.09170305676855894','36317391'),('0.05522682445759364','36576761'),('0.1428571428571429','36648204'),('0.14438502673796794','37786223'),('0.10132158590308371','38271760'),('0.15348837209302324','39267739'),('0.13095238095238093','41160587'),('0.12090680100755669','43272050'),('0.2191780821917808','43403127'),('0.11692307692307691','44903085'),('0.0680628272251309','47791562'),('0.1367924528301887','47868246'),('0.10204081632653061','49142760'),('0.37169215829084734','49631892'),('0.08242950108459868','51030552'),('0.1996512641673932','54191665'),('0.10716677829872745','56748733'),('0.19012345679012344','58485079'),('0.08712121212121215','61639371'),('0.16000000000000003','66692456'),('0.14077669902912626','66733002'),('0.23043478260869565','75937648'),('0.16296296296296298','77543886'),('0.3909090909090909','85816940'),('0.1169154228855721','94363275'),('0.05970149253731338','97340936'),('0.07942238267148016','99781740'),('0.2205491585473871','118754720'),('0.1017369727047146','120279132'),('0.25196850393700787','128912828'),('0.11044176706827313','135980509'),('0.046979865771812124','147983220'),('0.16083916083916083','157330863'),('0.10461538461538467','169528817'),('0.12276214833759591','174589427'),('0.19164619164619168','176135235'),('0.2883156297420334','194326389'),('0.11214953271028039','199168733'),('0.12681159420289856','225347042'),('0.23308270676691734','258592987'),('0.15139442231075695','258875006'),('0.297045101088647','269415357'),('0.25260960334029225','271887040'),('0.16317991631799167','283886865'),('0.11274509803921573','286113280'),('0.05993690851735012','292838396'),('0.2071197411003236','303246676'),('0.048192771084337394','313248263'),('0.18238213399503722','316381099'),('0.09090909090909094','320740464'),('0.11920529801324509','337827661'),('0.0955056179775281','343015985'),('0.26875529212531757','349991143'),('0.24012754476330633','351609538'),('0.36283185840707965','351856931'),('0.17572463768115942','353361863'),('0.16290130796670632','358695457'),('0.1314168377823408','364225566'),('0.1774744027303754','370687372'),('0.2835443037974683','370689210'),('0.13823208439432522','372984197'),('0.13738738738738743','373854628'),('0.16329966329966328','380829248'),('0.18706697459584298','385016070'),('0.08131868131868136','385281102'),('0.3467815049864007','386900246'),('0.07300884955752207','387108043'),('0.216349240316713','387636363'),('0.1608832807570978','390647282'),('0.12456747404844293','392505232'),('0.042424242424242475','393885664'),('0.07062146892655363','397244810'),('0.2329411764705882','399815233'),('0.052854122621564525','401480763'),('0.20778239516433694','402417817'),('0.10187424425634828','406805563'),('0.18986216096042685','407106379'),('0.15471698113207544','410520501'),('0.16981132075471694','410741448'),('0.1800699300699301','416622817'),('0.16018423746161714','420249427'),('0.11006910167818362','421267475'),('0.16326530612244894','421347849'),('0.1189320388349514','422501642'),('0.1331444759206799','423902976'),('0','430219038'),('0.09677419354838712','431311100'),('0.30823529411764705','431473020'),('0.2555231346394331','434334701'),('0.23133116883116878','434401868'),('0.2906481273828213','434563934'),('0.17154882154882156','434565011'),('0.1301859799713877','434662713'),('0.09463722397476337','436693674'),('0.06584362139917699','436809386'),('0.05707196029776673','437786939'),('0.1834862385321101','438756539'),('0.09433962264150941','438848253'),('0.10355029585798814','439071630'),('0.19882396177875783','441381282'),('0.11927330173775674','441382432'),('0.052208835341365445','441952268'),('0.3189252336448598','442426299'),('0.029687499999999978','442902274'),('0.04235294117647059','451377668'),('0.1094527363184079','455899334'),('0.08394160583941601','456749835'),('0.2505353319057816','471460273'),('0.6704119850187267','471723540'),('0.15294117647058825','472056419'),('0.06329113924050633','472360498'),('0.0665188470066519','472821519'),('0.07664233576642332','472845978'),('0.05544147843942504','472848826'),('0.10834813499111906','472877684'),('0.05882352941176472','473764233'),('0.286096256684492','474369808'),('0.12064965197215782','474593909'),('0.07180851063829785','474593910'),('0.13903743315508021','474856218'),('0.047008547008547064','476542825'),('0.050793650793650835','476676325'),('0.23830409356725146','476725595'),('0.17307692307692313','477306079'),('0.1270718232044199','477317922'),('0.17870257037943693','477332594'),('0.16666666666666663','477342747'),('0.12647554806070826','479633069'),('0.11012433392539966','480248442'),('0.047272727272727244','480432362'),('0.0714285714285714','480536263'),('0.3153649419634075','480680646'),('0.16614173228346452','480745939'),('0.14022140221402213','481694509'),('0.07262569832402233','482911295'),('0.3888213851761847','484322035'),('0.15186915887850472','484451346'),('0.1074380165289256','484660274'),('0.07322175732217573','486618657'),('0.2180746561886051','486997652'),('0.17272987682612428','487550002'),('0.22033898305084743','488970166'),('0.0905432595573441','489146840'),('0.06557377049180324','489772340'),('0.10407239819004521','490331391'),('0.08187134502923976','491652986'),('0.10617283950617284','494850406'),('0.1412300683371298','495707763'),('0.1991434689507494','497430637'),('0.1182519280205655','497677999'),('0.06639004149377592','498506274'),('0.2471380471380471','508963009'),('0.224390243902439','509050400'),('0.09580838323353291','513273343'),('0.16279069767441856','517746113'),('0.24395161290322576','521950190'),('0.06970509383378021','523922454'),('0.09826589595375723','524086947'),('0.2709677419354839','524279657'),('0.09952606635071093','524303239'),('0.09126213592233012','525105971'),('0.22395833333333337','528497581'),('0.1282051282051282','534982695'),('0.14359712230215826','541696090'),('0.040462427745664775','547498202'),('0.13850415512465375','549256707'),('0.10780669144981414','550457147'),('0.06496519721577731','551527845'),('0.06182795698924726','558070433'),('0.1116751269035533','558070434'),('0.08869179600886923','558070436'),('0.03180212014134276','558984017'),('0.08823529411764708','567234492'),('0.16425992779783394','571841213'),('0.034168564920273314','573930836'),('0.4091627172195893','574317507'),('0.05238095238095242','576858552'),('0.1403162055335968','591892279'),('0.388235294117647','592507317'),('0.10023866348448685','601481495'),('0.0725490196078431','602200741'),('0.08092485549132944','602724685'),('0.11407766990291257','606293627'),('0.06140350877192979','613345189'),('0.15639730639730642','617459493'),('0.11934900542495475','623441609'),('0.09311616472034423','623441612'),('0.08074534161490687','627882362'),('0.06208425720620847','631070414'),('0.08774193548387099','646432928'),('0.06796116504854366','647575049'),('0.05240174672489084','650573749'),('0.18202247191011234','650663945'),('0.12765957446808507','663577831'),('0.308584686774942','664047468'),('0.09635416666666663','666726799'),('0.16222222222222227','666726800'),('0.11130742049469966','666726801'),('0.08108108108108103','666726802'),('0.049792531120331995','666726803'),('0.0662650602409639','667042223'),('0.1063829787234043','671538942'),('0.08571428571428574','671738413'),('0.2585858585858586','672328094'),('0.24090909090909096','672342685'),('0.26622516556291387','672346917'),('0.3011935408378189','672353429'),('0.3677510608203678','674539396'),('0.08999999999999997','674839637'),('0.3306878306878307','686241472'),('0.11333333333333329','688053738'),('0.11083743842364535','688275304'),('0.05136986301369861','688335924'),('0.11848341232227488','688496841'),('0.07857142857142863','690147772'),('0.07407407407407407','690608686'),('0.07910750507099396','690608687'),('0.03385416666666663','690608688'),('0.09403669724770647','690608691'),('0.09002770083102496','690608693'),('0.08740359897172234','690608694'),('0.02487562189054726','690608696'),('0.052896725440806036','690608702'),('0.09534368070953436','690608704'),('0.1809145129224652','690608706'),('0.07608695652173914','690804827'),('0.13550536838208072','692283831'),('0.027027027027026973','692437895'),('0.14803625377643503','692611676'),('0.15558698727015563','697091119'),('0.060948081264108334','697652272'),('0.11934604904632151','698029620'),('0.16019935920256323','698438232'),('0.12107623318385652','699094856'),('0.09823677581863977','700818858'),('0.049707602339181256','701272072'),('0.09109311740890691','703007996'),('0.0625','703018634'),('0.059523809523809534','1010093017'),('0.11737089201877937','1033698887'),('0.05681818181818177','1043321643'),('0.07427055702917773','1048861669'),('0.1741573033707865','1056281929'),('0.44744744744744747','1062342323'),('0.1406810035842294','1089059487'),('0.20411663807890223','1090010845'),('0.06580293215138089','1096223397'),('0.10236220472440949','1097496558'),('0.04986876640419946','1112031857'),('0.06451612903225812','1147353799'),('0.15398886827458258','1164975438'),('0.058978102189781056','1202504814'),('0.0515759312320917','1202562007'),('0.13745704467353947','1202948480'),('0.21171171171171166','1205886701'),('0.036036036036036','1220621189'),('0.12354312354312358','1243266187'),('0.14487300094073374','1265680561'),('0.10729613733905574','1267463286'),('0.13714285714285712','1289434903'),('0.16666666666666663','1322881625'),('0.08247422680412375','1355412269'),('0.006896551724137945','1376650682'),('0.08445945945945943','1420419918'),('0.03968253968253965','1434788295'),('0.2518101367658889','1437582453'),('0.24608967674661109','1472906636'),('0.10245901639344257','1489377760'),('0.082018927444795','1501380958'),('0.1029411764705882','1508519945'),('0.14942528735632188','1520905828'),('0.04705882352941182','1560641990'),('0.07407407407407407','1570473318'),('0.03682719546742208','1589117610'),('0.09268292682926826','1601919108'),('0.04278074866310155','1617739681'),('0.03350515463917525','1658229747'),('0.04797979797979801','1658766768'),('0.11855670103092786','1666306454'),('0.12692307692307692','1705007318'),('0.14099216710182771','1721741513'),('0.022058823529411797','1731513328'),('0.08436213991769548','1734978373'),('0.04219409282700426','1761499833'),('0.04166666666666663','1765846847'),('0.07317073170731703','1766612829'),('0.11704312114989734','1780255602'),('0.2591006423982869','1802011210'),('0.1507246376811594','1825301994'),('0.11373390557939911','1828506816'),('0.15040650406504064','1844102339'),('0.039312039312039304','1846208014'),('0.10196078431372546','1849519124'),('0.23244929797191882','1861416807'),('0.08078602620087338','1875094289'),('0.05232558139534882','1899153123'),('0.2775068899724401','1900434152'),('0.12090680100755669','1910896691'),('0.12669193286410396','1926156228'),('0.08310991957104563','1964786482'),('0.2849740932642487','1968783589'),('0.1444444444444445','1970998002'),('0.11924686192468614','1994541396'),('0.07981220657277','2036015357'),('0.18074074074074076','2052064438'),('0.08805031446540879','2094031249'),('0.09181141439205953','2100944625'),('0.06896551724137934','2103954767'),('0.09933774834437081','2111566071'),('0.05679012345679013','2115139772'),('0.12941176470588234','2123631024'),('0.06542056074766356','2123801125'),('0.07725321888412018','2138602891'),('0.1345076060848679','2143967328'),('0.029612756264236872','693');
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-26 14:47:32
