Sääaseman toteutus Raspberry Pi Pico -mikrokontrollerilla (Wokwi-simulaattori)
Projektissani toteutin IoT-pohjaisen sääaseman käyttäen Wokwi-simulaattoria ja Raspberry Pi Pico -mikrokontrolleria. Kokonaisuus muodostaa yksinkertaisen IoT-pipeline-rakenteen, jossa sensorilta kerätty data siirtyy usean teknologian läpi aina visuaaliseen esitykseen asti.

Laitteisto ja sensorointi
Sääasema hyödyntää DHT22-sensoria, joka mittaa lämpötilan ja kosteuden. Sensorin lukemat käsitellään Raspberry Pi Picon avulla, ja ne näytetään I2C-liitännäisellä LCD-näytöllä. Näytölle tulostetaan reaaliaikainen lämpötila, ja lisäksi näyttö antaa yksinkertaisen sanallisen kommentin lämpötilan luonteesta (esim. "Kylmä", "Lämmin").

Tiedonsiirto ja verkkoyhteydet
Laite yhdistetään Wi-Fi-verkkoon Wokwi-simulaattorin kautta. Kun yhteys on muodostettu, Pico lähettää sensorilta saadut arvot eteenpäin ThingSpeak-palveluun HTTP POST -pyynnön avulla. Tämä tapahtuu käyttämällä ThingSpeakin Write API Key -avainta, joka autentikoi datan lähetyksen.

Pilvipalvelu ja datan keräys
ThingSpeak toimii projektissa API endpointina, johon laite lähettää mittaustiedot. Palvelu tallentaa nämä arvot kenttiin, joita voidaan myöhemmin hakea Read API Keyn avulla. ThingSpeak tarjoaa myös mahdollisuuden käyttää webhookeja tai websocket-yhteyksiä reaaliaikaisen datan siirtoon, mutta tässä projektissa käytettiin perinteistä HTTP-pohjaista tiedonsiirtoa.

Visualisointi ja HTML-kaavio
Kerätty data haetaan ThingSpeakin JSON-rajapinnasta ja visualisoidaan omassa HTML-tiedostossa. Tiedosto hyödyntää Chart.js-kirjastoa, jolla piirretään interaktiivinen viivakaavio lämpötilan kehityksestä. Kaavio on skaalattu sopimaan pienelle näytölle, ja se päivittyy automaattisesti uusimman datan perusteella.

Yhteenveto
Projektissa yhdistyvät seuraavat keskeiset IoT-teknologiat:

Sensorointi: DHT22 mittaa lämpötilan ja kosteuden.

Edge-laskenta: Raspberry Pi Pico käsittelee ja lähettää datan.

Pilvitallennus: ThingSpeak vastaanottaa ja säilyttää mittaustiedot.

API endpoint: JSON-rajapinta mahdollistaa datan hakemisen.

Visualisointi: HTML + Chart.js esittää datan kaaviona.

IoT-pipeline: koko ketju sensorista selaimeen muodostaa toimivan tiedonvälityspolun.

Tämä projekti toimii esimerkkinä siitä, miten yksinkertaisilla komponenteilla voidaan rakentaa toimiva ja skaalautuva IoT-järjestelmä, joka yhdistää laitteiston, verkkoyhteyden, pilvipalvelun ja web-teknologiat.
