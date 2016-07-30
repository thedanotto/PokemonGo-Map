#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import requests
from peewee import Model, SqliteDatabase, InsertQuery, IntegerField,\
                   CharField, FloatField, BooleanField, DateTimeField
from datetime import datetime
from datetime import timedelta
from base64 import b64encode



from .utils import get_pokemon_name, get_args
from .transform import transform_from_wgs_to_gcj
from .customLog import printPokemon

args = get_args()
db = SqliteDatabase(args.db)
log = logging.getLogger(__name__)


class BaseModel(Model):
    class Meta:
        database = db

    @classmethod
    def get_all(cls):
        results = [m for m in cls.select().dicts()]
        if args.china:
            for result in results:
                result['latitude'],  result['longitude'] = \
                    transform_from_wgs_to_gcj(result['latitude'],  result['longitude'])
        return results


class Pokemon(BaseModel):
    # We are base64 encoding the ids delivered by the api
    # because they are too big for sqlite to handle
    encounter_id = CharField(primary_key=True)
    spawnpoint_id = CharField()
    pokemon_id = IntegerField()
    latitude = FloatField()
    longitude = FloatField()
    disappear_time = DateTimeField()

    @classmethod
    def get_active(cls):
        query = (Pokemon
                 .select()
                 .where(Pokemon.disappear_time > datetime.utcnow())
                 .dicts())

        pokemons = []
        for p in query:
            p['pokemon_name'] = get_pokemon_name(p['pokemon_id'])
            if args.china:
                p['latitude'], p['longitude'] = \
                    transform_from_wgs_to_gcj(p['latitude'], p['longitude'])
            pokemons.append(p)

        return pokemons

    @classmethod
    def report_active(cls):
        query = (Pokemon
                 .select()
                 .where(Pokemon.disappear_time > datetime.utcnow())
                 .dicts())

        pokemons = []
        wanted_pokemon = []
        # comment out unwanted pokemon
        wanted_pokemon.append("Bulbasaur")
        wanted_pokemon.append("Ivysaur")
        wanted_pokemon.append("Venusaur")
        wanted_pokemon.append("Charmander")
        wanted_pokemon.append("Charmeleon")
        wanted_pokemon.append("Charizard")
        wanted_pokemon.append("Squirtle")
        wanted_pokemon.append("Wartortle")
        wanted_pokemon.append("Blastoise")
        #wanted_pokemon.append("Caterpie")
        #wanted_pokemon.append("Metapod")
        wanted_pokemon.append("Butterfree")
        #wanted_pokemon.append("Weedle")
        #wanted_pokemon.append("Kakuna")
        wanted_pokemon.append("Beedrill")
        #wanted_pokemon.append("Pidgey")
        #wanted_pokemon.append("Pidgeotto")
        #wanted_pokemon.append("Pidgeot")
        #wanted_pokemon.append("Rattata")
        #wanted_pokemon.append("Raticate")
        #wanted_pokemon.append("Spearow")
        wanted_pokemon.append("Fearow")
        #wanted_pokemon.append("Ekans")
        #wanted_pokemon.append("Arbok")
        wanted_pokemon.append("Pikachu")
        wanted_pokemon.append("Raichu")
        wanted_pokemon.append("Sandshrew")
        wanted_pokemon.append("Sandslash")
        #wanted_pokemon.append("Nidoran♀")
        wanted_pokemon.append("Nidorina")
        wanted_pokemon.append("Nidoqueen")
        #wanted_pokemon.append("Nidoran♂")
        wanted_pokemon.append("Nidorino")
        wanted_pokemon.append("Nidoking")
        #wanted_pokemon.append("Clefairy")
        wanted_pokemon.append("Clefable")
        wanted_pokemon.append("Vulpix")
        wanted_pokemon.append("Ninetales")
        wanted_pokemon.append("Jigglypuff")
        wanted_pokemon.append("Wigglytuff")
        #wanted_pokemon.append("Zubat")
        #wanted_pokemon.append("Golbat")
        #wanted_pokemon.append("Oddish")
        wanted_pokemon.append("Gloom")
        wanted_pokemon.append("Vileplume")
        #wanted_pokemon.append("Paras")
        wanted_pokemon.append("Parasect")
        #wanted_pokemon.append("Venonat")
        wanted_pokemon.append("Venomoth")
        wanted_pokemon.append("Diglett")
        wanted_pokemon.append("Dugtrio")
        wanted_pokemon.append("Meowth")
        wanted_pokemon.append("Persian")
        wanted_pokemon.append("Psyduck")
        wanted_pokemon.append("Golduck")
        #wanted_pokemon.append("Mankey")
        wanted_pokemon.append("Primeape")
        wanted_pokemon.append("Growlithe")
        wanted_pokemon.append("Arcanine")
        #wanted_pokemon.append("Poliwag")
        wanted_pokemon.append("Poliwhirl")
        wanted_pokemon.append("Poliwrath")
        #wanted_pokemon.append("Abra")
        wanted_pokemon.append("Kadabra")
        wanted_pokemon.append("Alakazam")
        wanted_pokemon.append("Machop")
        wanted_pokemon.append("Machoke")
        wanted_pokemon.append("Machamp")
        #wanted_pokemon.append("Bellsprout")
        #wanted_pokemon.append("Weepinbell")
        wanted_pokemon.append("Victreebel")
        wanted_pokemon.append("Tentacool")
        wanted_pokemon.append("Tentacruel")
        #wanted_pokemon.append("Geodude")
        wanted_pokemon.append("Graveler")
        wanted_pokemon.append("Golem")
        wanted_pokemon.append("Ponyta")
        wanted_pokemon.append("Rapidash")
        wanted_pokemon.append("Slowpoke")
        wanted_pokemon.append("Slowbro")
        wanted_pokemon.append("Magnemite")
        wanted_pokemon.append("Magneton")
        wanted_pokemon.append("Farfetch'd")
        #wanted_pokemon.append("Doduo")
        wanted_pokemon.append("Dodrio")
        wanted_pokemon.append("Seel")
        wanted_pokemon.append("Dewgong")
        wanted_pokemon.append("Grimer")
        wanted_pokemon.append("Muk")
        wanted_pokemon.append("Shellder")
        wanted_pokemon.append("Cloyster")
        wanted_pokemon.append("Gastly")
        wanted_pokemon.append("Haunter")
        wanted_pokemon.append("Gengar")
        wanted_pokemon.append("Onix")
        wanted_pokemon.append("Drowzee")
        wanted_pokemon.append("Hypno")
        #wanted_pokemon.append("Krabby")
        wanted_pokemon.append("Kingler")
        wanted_pokemon.append("Voltorb")
        wanted_pokemon.append("Electrode")
        wanted_pokemon.append("Exeggcute")
        wanted_pokemon.append("Exeggutor")
        wanted_pokemon.append("Cubone")
        wanted_pokemon.append("Marowak")
        wanted_pokemon.append("Hitmonlee")
        wanted_pokemon.append("Hitmonchan")
        wanted_pokemon.append("Lickitung")
        wanted_pokemon.append("Koffing")
        wanted_pokemon.append("Weezing")
        wanted_pokemon.append("Rhyhorn")
        wanted_pokemon.append("Rhydon")
        wanted_pokemon.append("Chansey")
        wanted_pokemon.append("Tangela")
        wanted_pokemon.append("Kangaskhan")
        #wanted_pokemon.append("Horsea")
        #wanted_pokemon.append("Seadra")
        #wanted_pokemon.append("Goldeen")
        wanted_pokemon.append("Seaking")
        #wanted_pokemon.append("Staryu")
        wanted_pokemon.append("Starmie")
        wanted_pokemon.append("Mr. Mime")
        wanted_pokemon.append("Scyther")
        wanted_pokemon.append("Jynx")
        wanted_pokemon.append("Electabuzz")
        wanted_pokemon.append("Magmar")
        wanted_pokemon.append("Pinsir")
        wanted_pokemon.append("Tauros")
        #wanted_pokemon.append("Magikarp")
        wanted_pokemon.append("Gyarados")
        wanted_pokemon.append("Lapras")
        wanted_pokemon.append("Ditto")
        #wanted_pokemon.append("Eevee")
        wanted_pokemon.append("Vaporeon")
        wanted_pokemon.append("Jolteon")
        wanted_pokemon.append("Flareon")
        wanted_pokemon.append("Porygon")
        wanted_pokemon.append("Omanyte")
        wanted_pokemon.append("Omastar")
        wanted_pokemon.append("Kabuto")
        wanted_pokemon.append("Kabutops")
        wanted_pokemon.append("Aerodactyl")
        wanted_pokemon.append("Snorlax")
        wanted_pokemon.append("Articuno")
        wanted_pokemon.append("Zapdos")
        wanted_pokemon.append("Moltres")
        wanted_pokemon.append("Dratini")
        wanted_pokemon.append("Dragonair")
        wanted_pokemon.append("Dragonite")
        wanted_pokemon.append("Mewtwo")

        for p in query:
            p['pokemon_name'] = get_pokemon_name(p['pokemon_id'])
            pokemon_name = get_pokemon_name(p['pokemon_id'])

            if args.china:
                p['latitude'], p['longitude'] = \
                    transform_from_wgs_to_gcj(p['latitude'], p['longitude'])
            pokemons.append(p)

            disappears_in_unformatted = p['disappear_time'] - datetime.utcnow()
            disappears_in = str(timedelta(seconds=disappears_in_unformatted.seconds)) # removes the .2314324 from the end
            pokemon_alert_text = "%s nearby! It disappears in %s Apple Maps: <http://maps.apple.com/?saddr=36.142919,-86.767305&daddr=%s,%s> Google Maps: <https://www.google.com/maps/dir/36.142919,-86.767305/%s,%s>" % (p['pokemon_name'], disappears_in, p['latitude'], p['longitude'], p['latitude'], p['longitude'])
            is_pokemon_wanted =  pokemon_name in wanted_pokemon
            log.info("%s" % p['encounter_id'])
            if is_pokemon_wanted:
                # yes, we want to be alerted of that pokemon
                log.info(pokemon_alert_text)
                r = requests.post("https://hooks.slack.com/services/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", headers={"ContType": "application/json"}, json={"channel": "#pokemon", "username": "pokescout", "text": pokemon_alert_text, "icon_emoji": ":ghost:"})
            else:
                # no, we dont want to be alerted of that pokemon
                log.info("%s was not in the wanted list" % p['pokemon_name'])

        return pokemons


class Pokestop(BaseModel):
    pokestop_id = CharField(primary_key=True)
    enabled = BooleanField()
    latitude = FloatField()
    longitude = FloatField()
    last_modified = DateTimeField()
    lure_expiration = DateTimeField(null=True)
    active_pokemon_id = IntegerField(null=True)


class Gym(BaseModel):
    UNCONTESTED = 0
    TEAM_MYSTIC = 1
    TEAM_VALOR = 2
    TEAM_INSTINCT = 3

    gym_id = CharField(primary_key=True)
    team_id = IntegerField()
    guard_pokemon_id = IntegerField()
    gym_points = IntegerField()
    enabled = BooleanField()
    latitude = FloatField()
    longitude = FloatField()
    last_modified = DateTimeField()

class ScannedLocation(BaseModel):
    scanned_id = CharField(primary_key=True)
    latitude = FloatField()
    longitude = FloatField()
    last_modified = DateTimeField()

    @classmethod
    def get_recent(cls):
        query = (ScannedLocation
                 .select()
                 .where(ScannedLocation.last_modified >= (datetime.utcnow() - timedelta(minutes=15)))
                 .dicts())

        scans = []
        for s in query:
            scans.append(s)

        return scans

def parse_map(map_dict, iteration_num, step, step_location):
    pokemons = {}
    pokestops = {}
    gyms = {}
    scanned = {}

    cells = map_dict['responses']['GET_MAP_OBJECTS']['map_cells']
    for cell in cells:
        for p in cell.get('wild_pokemons', []):
            d_t = datetime.utcfromtimestamp(
                (p['last_modified_timestamp_ms'] +
                 p['time_till_hidden_ms']) / 1000.0)
            printPokemon(p['pokemon_data']['pokemon_id'],p['latitude'],p['longitude'],d_t)
            pokemons[p['encounter_id']] = {
                'encounter_id': b64encode(str(p['encounter_id'])),
                'spawnpoint_id': p['spawnpoint_id'],
                'pokemon_id': p['pokemon_data']['pokemon_id'],
                'latitude': p['latitude'],
                'longitude': p['longitude'],
                'disappear_time': d_t
            }

        if iteration_num > 0 or step > 50:
            for f in cell.get('forts', []):
                if f.get('type') == 1:  # Pokestops
                        if 'lure_info' in f:
                            lure_expiration = datetime.utcfromtimestamp(
                                f['lure_info']['lure_expires_timestamp_ms'] / 1000.0)
                            active_pokemon_id = f['lure_info']['active_pokemon_id']
                        else:
                            lure_expiration, active_pokemon_id = None, None

                        pokestops[f['id']] = {
                            'pokestop_id': f['id'],
                            'enabled': f['enabled'],
                            'latitude': f['latitude'],
                            'longitude': f['longitude'],
                            'last_modified': datetime.utcfromtimestamp(
                                f['last_modified_timestamp_ms'] / 1000.0),
                            'lure_expiration': lure_expiration,
                            'active_pokemon_id': active_pokemon_id
                    }

                else:  # Currently, there are only stops and gyms
                    gyms[f['id']] = {
                        'gym_id': f['id'],
                        'team_id': f.get('owned_by_team', 0),
                        'guard_pokemon_id': f.get('guard_pokemon_id', 0),
                        'gym_points': f.get('gym_points', 0),
                        'enabled': f['enabled'],
                        'latitude': f['latitude'],
                        'longitude': f['longitude'],
                        'last_modified': datetime.utcfromtimestamp(
                            f['last_modified_timestamp_ms'] / 1000.0),
                    }

    if pokemons:
        log.info("Upserting {} pokemon".format(len(pokemons)))
        bulk_upsert(Pokemon, pokemons)

    if pokestops:
        log.info("Upserting {} pokestops".format(len(pokestops)))
        bulk_upsert(Pokestop, pokestops)

    if gyms:
        log.info("Upserting {} gyms".format(len(gyms)))
        bulk_upsert(Gym, gyms)

    scanned[0] = {
        'scanned_id': str(step_location[0])+','+str(step_location[1]),
        'latitude': step_location[0],
        'longitude': step_location[1],
        'last_modified': datetime.utcnow(),
    }

    bulk_upsert(ScannedLocation, scanned)

def bulk_upsert(cls, data):
    num_rows = len(data.values())
    i = 0
    step = 120

    while i < num_rows:
        log.debug("Inserting items {} to {}".format(i, min(i+step, num_rows)))
        InsertQuery(cls, rows=data.values()[i:min(i+step, num_rows)]).upsert().execute()
        i+=step



def create_tables():
    db.connect()
    db.create_tables([Pokemon, Pokestop, Gym, ScannedLocation], safe=True)
    db.close()
