import typing
import configparser


def nm_parse_nmconnection_keyfile(content: str) -> dict[str, typing.Any]:
    config = configparser.ConfigParser()
    config.read_string(content)
    sections: list[str] = config.sections()
    data: dict[str, typing.Any] = {'_keys': sections}
    for section in sections:
        data[section] = dict(config[section])
        data[section]['_keys'] = list(config[section].keys())
    return data


class FilterModule(object):

    def filters(self):
        return {
            'nm_parse_nmconnection_keyfile': nm_parse_nmconnection_keyfile,
        }
