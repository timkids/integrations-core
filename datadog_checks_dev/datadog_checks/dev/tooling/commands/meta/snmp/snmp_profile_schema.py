# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

def get_profile_schema():
    #extends (optional)
    #device:
        #vendor
    #sysobjectid
    #validate the schema? https://python-jsonschema.readthedocs.io/en/stable/validate/#jsonschema.IValidator.check_schema
    return({
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "extends": [
                "_base.yaml",
                "_generic-ip.yaml"
            ],
            "device": {
                "vendor": "f5"
            },
            "sysobjectid": "1.3.6.1.4.1.3375.2.1.3.4.*",
            "metrics": [
                {
                    "MIB": "F5-BIGIP-SYSTEM-MIB",
                    "forced_type": "gauge",
                    "symbol": {
                        "OID": "1.3.6.1.4.1.3375.2.1.1.2.1.44.0",
                        "name": "sysStatMemoryTotal"
                    }
                },
                {
                    "MIB": "F5-BIGIP-LOCAL-MIB",
                    "table": {
                        "OID": "1.3.6.1.4.1.3375.2.2.10.1.2",
                        "name": "ltmVirtualServTable"
                    },
                    "symbols": [
                        {
                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.9",
                            "name": "ltmVirtualServEnabled"
                        },
                        {
                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.10",
                            "name": "ltmVirtualServConnLimit"
                        }
                    ],
                    "metric_tags": [
                        {
                            "tag": "server",
                            "column": {
                                "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.1",
                                "name": "ltmVirtualServName"
                            }
                        }
                    ]
                }
            ],
            "metric_tags": [
                {
                    "OID": "1.3.6.1.2.1.1.5.0",
                    "symbol": "sysName",
                    "tag": "snmp_host"
                }
            ]
        }
    ],
    "required": [],
    "properties": {
        "extends": {
            "$id": "#/properties/extends",
            "type": "array",
            "title": "The extends schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    "_base.yaml",
                    "_generic-ip.yaml"
                ]
            ],
            "additionalItems": True,
            "items": {
                "$id": "#/properties/extends/items",
                "anyOf": [
                    {
                        "$id": "#/properties/extends/items/anyOf/0",
                        "type": "string",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "_base.yaml",
                            "_generic-ip.yaml"
                        ]
                    }
                ]
            }
        },
        "device": {
            "$id": "#/properties/device",
            "type": "object",
            "title": "The device schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "vendor": "f5"
                }
            ],
            "required": [
                "vendor"
            ],
            "properties": {
                "vendor": {
                    "$id": "#/properties/device/properties/vendor",
                    "type": "string",
                    "title": "The vendor schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "f5"
                    ]
                }
            },
            "additionalProperties": True
        },
        "sysobjectid": {
            "$id": "#/properties/sysobjectid",
            "type": "string",
            "title": "The sysobjectid schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1.3.6.1.4.1.3375.2.1.3.4.*"
            ]
        },
        "metrics": {
            "$id": "#/properties/metrics",
            "type": "array",
            "title": "The metrics schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "MIB": "F5-BIGIP-SYSTEM-MIB",
                        "forced_type": "gauge",
                        "symbol": {
                            "OID": "1.3.6.1.4.1.3375.2.1.1.2.1.44.0",
                            "name": "sysStatMemoryTotal"
                        }
                    },
                    {
                        "MIB": "F5-BIGIP-LOCAL-MIB",
                        "table": {
                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2",
                            "name": "ltmVirtualServTable"
                        },
                        "symbols": [
                            {
                                "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.9",
                                "name": "ltmVirtualServEnabled"
                            },
                            {
                                "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.10",
                                "name": "ltmVirtualServConnLimit"
                            }
                        ],
                        "metric_tags": [
                            {
                                "tag": "server",
                                "column": {
                                    "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.1",
                                    "name": "ltmVirtualServName"
                                }
                            }
                        ]
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "$id": "#/properties/metrics/items",
                "anyOf": [
                    {
                        "$id": "#/properties/metrics/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "MIB": "F5-BIGIP-SYSTEM-MIB",
                                "forced_type": "gauge",
                                "symbol": {
                                    "OID": "1.3.6.1.4.1.3375.2.1.1.2.1.44.0",
                                    "name": "sysStatMemoryTotal"
                                }
                            }
                        ],
                        "required": [
                            "MIB",
                            "forced_type",
                            "symbol"
                        ],
                        "properties": {
                            "MIB": {
                                "$id": "#/properties/metrics/items/anyOf/0/properties/MIB",
                                "type": "string",
                                "title": "The MIB schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "F5-BIGIP-SYSTEM-MIB"
                                ]
                            },
                            "forced_type": {
                                "$id": "#/properties/metrics/items/anyOf/0/properties/forced_type",
                                "type": "string",
                                "title": "The forced_type schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "gauge"
                                ]
                            },
                            "symbol": {
                                "$id": "#/properties/metrics/items/anyOf/0/properties/symbol",
                                "type": "object",
                                "title": "The symbol schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": {},
                                "examples": [
                                    {
                                        "OID": "1.3.6.1.4.1.3375.2.1.1.2.1.44.0",
                                        "name": "sysStatMemoryTotal"
                                    }
                                ],
                                "required": [
                                    "OID",
                                    "name"
                                ],
                                "properties": {
                                    "OID": {
                                        "$id": "#/properties/metrics/items/anyOf/0/properties/symbol/properties/OID",
                                        "type": "string",
                                        "title": "The OID schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "1.3.6.1.4.1.3375.2.1.1.2.1.44.0"
                                        ]
                                    },
                                    "name": {
                                        "$id": "#/properties/metrics/items/anyOf/0/properties/symbol/properties/name",
                                        "type": "string",
                                        "title": "The name schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "sysStatMemoryTotal"
                                        ]
                                    }
                                },
                                "additionalProperties": True
                            }
                        },
                        "additionalProperties": True
                    },
                    {
                        "$id": "#/properties/metrics/items/anyOf/1",
                        "type": "object",
                        "title": "The second anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "MIB": "F5-BIGIP-LOCAL-MIB",
                                "table": {
                                    "OID": "1.3.6.1.4.1.3375.2.2.10.1.2",
                                    "name": "ltmVirtualServTable"
                                },
                                "symbols": [
                                    {
                                        "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.9",
                                        "name": "ltmVirtualServEnabled"
                                    },
                                    {
                                        "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.10",
                                        "name": "ltmVirtualServConnLimit"
                                    }
                                ],
                                "metric_tags": [
                                    {
                                        "tag": "server",
                                        "column": {
                                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.1",
                                            "name": "ltmVirtualServName"
                                        }
                                    }
                                ]
                            }
                        ],
                        "required": [
                            "MIB",
                            "table",
                            "symbols",
                            "metric_tags"
                        ],
                        "properties": {
                            "MIB": {
                                "$id": "#/properties/metrics/items/anyOf/1/properties/MIB",
                                "type": "string",
                                "title": "The MIB schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "F5-BIGIP-LOCAL-MIB"
                                ]
                            },
                            "table": {
                                "$id": "#/properties/metrics/items/anyOf/1/properties/table",
                                "type": "object",
                                "title": "The table schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": {},
                                "examples": [
                                    {
                                        "OID": "1.3.6.1.4.1.3375.2.2.10.1.2",
                                        "name": "ltmVirtualServTable"
                                    }
                                ],
                                "required": [
                                    "OID",
                                    "name"
                                ],
                                "properties": {
                                    "OID": {
                                        "$id": "#/properties/metrics/items/anyOf/1/properties/table/properties/OID",
                                        "type": "string",
                                        "title": "The OID schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "1.3.6.1.4.1.3375.2.2.10.1.2"
                                        ]
                                    },
                                    "name": {
                                        "$id": "#/properties/metrics/items/anyOf/1/properties/table/properties/name",
                                        "type": "string",
                                        "title": "The name schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "ltmVirtualServTable"
                                        ]
                                    }
                                },
                                "additionalProperties": True
                            },
                            "symbols": {
                                "$id": "#/properties/metrics/items/anyOf/1/properties/symbols",
                                "type": "array",
                                "title": "The symbols schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": [],
                                "examples": [
                                    [
                                        {
                                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.9",
                                            "name": "ltmVirtualServEnabled"
                                        },
                                        {
                                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.10",
                                            "name": "ltmVirtualServConnLimit"
                                        }
                                    ]
                                ],
                                "additionalItems": True,
                                "items": {
                                    "$id": "#/properties/metrics/items/anyOf/1/properties/symbols/items",
                                    "anyOf": [
                                        {
                                            "$id": "#/properties/metrics/items/anyOf/1/properties/symbols/items/anyOf/0",
                                            "type": "object",
                                            "title": "The first anyOf schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": {},
                                            "examples": [
                                                {
                                                    "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.9",
                                                    "name": "ltmVirtualServEnabled"
                                                }
                                            ],
                                            "required": [
                                                "OID",
                                                "name"
                                            ],
                                            "properties": {
                                                "OID": {
                                                    "$id": "#/properties/metrics/items/anyOf/1/properties/symbols/items/anyOf/0/properties/OID",
                                                    "type": "string",
                                                    "title": "The OID schema",
                                                    "description": "An explanation about the purpose of this instance.",
                                                    "default": "",
                                                    "examples": [
                                                        "1.3.6.1.4.1.3375.2.2.10.1.2.1.9"
                                                    ]
                                                },
                                                "name": {
                                                    "$id": "#/properties/metrics/items/anyOf/1/properties/symbols/items/anyOf/0/properties/name",
                                                    "type": "string",
                                                    "title": "The name schema",
                                                    "description": "An explanation about the purpose of this instance.",
                                                    "default": "",
                                                    "examples": [
                                                        "ltmVirtualServEnabled"
                                                    ]
                                                }
                                            },
                                            "additionalProperties": True
                                        }
                                    ]
                                }
                            },
                            "metric_tags": {
                                "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags",
                                "type": "array",
                                "title": "The metric_tags schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": [],
                                "examples": [
                                    [
                                        {
                                            "tag": "server",
                                            "column": {
                                                "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.1",
                                                "name": "ltmVirtualServName"
                                            }
                                        }
                                    ]
                                ],
                                "additionalItems": True,
                                "items": {
                                    "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags/items",
                                    "anyOf": [
                                        {
                                            "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags/items/anyOf/0",
                                            "type": "object",
                                            "title": "The first anyOf schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": {},
                                            "examples": [
                                                {
                                                    "tag": "server",
                                                    "column": {
                                                        "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.1",
                                                        "name": "ltmVirtualServName"
                                                    }
                                                }
                                            ],
                                            "required": [
                                                "tag",

                                            ],
                                            "properties": {
                                                "tag": {
                                                    "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags/items/anyOf/0/properties/tag",
                                                    "type": "string",
                                                    "title": "The tag schema",
                                                    "description": "An explanation about the purpose of this instance.",
                                                    "default": "",
                                                    "examples": [
                                                        "server"
                                                    ]
                                                },
                                                "column": {
                                                    "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags/items/anyOf/0/properties/column",
                                                    "type": "object",
                                                    "title": "The column schema",
                                                    "description": "An explanation about the purpose of this instance.",
                                                    "default": {},
                                                    "examples": [
                                                        {
                                                            "OID": "1.3.6.1.4.1.3375.2.2.10.1.2.1.1",
                                                            "name": "ltmVirtualServName"
                                                        }
                                                    ],
                                                    "required": [
                                                        "OID",
                                                        "name"
                                                    ],
                                                    "properties": {
                                                        "OID": {
                                                            "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags/items/anyOf/0/properties/column/properties/OID",
                                                            "type": "string",
                                                            "title": "The OID schema",
                                                            "description": "An explanation about the purpose of this instance.",
                                                            "default": "",
                                                            "examples": [
                                                                "1.3.6.1.4.1.3375.2.2.10.1.2.1.1"
                                                            ]
                                                        },
                                                        "name": {
                                                            "$id": "#/properties/metrics/items/anyOf/1/properties/metric_tags/items/anyOf/0/properties/column/properties/name",
                                                            "type": "string",
                                                            "title": "The name schema",
                                                            "description": "An explanation about the purpose of this instance.",
                                                            "default": "",
                                                            "examples": [
                                                                "ltmVirtualServName"
                                                            ]
                                                        }
                                                    },
                                                    "additionalProperties": True
                                                }
                                            },
                                            "additionalProperties": True
                                        }
                                    ]
                                }
                            }
                        },
                        "additionalProperties": True
                    }
                ]
            }
        },
        "metric_tags": {
            "$id": "#/properties/metric_tags",
            "type": "array",
            "title": "The metric_tags schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "OID": "1.3.6.1.2.1.1.5.0",
                        "symbol": "sysName",
                        "tag": "snmp_host"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "$id": "#/properties/metric_tags/items",
                "anyOf": [
                    {
                        "$id": "#/properties/metric_tags/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "OID": "1.3.6.1.2.1.1.5.0",
                                "symbol": "sysName",
                                "tag": "snmp_host"
                            }
                        ],
                        "required": [
                            "OID",
                            "symbol",
                            "tag"
                        ],
                        "properties": {
                            "OID": {
                                "$id": "#/properties/metric_tags/items/anyOf/0/properties/OID",
                                "type": "string",
                                "title": "The OID schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "1.3.6.1.2.1.1.5.0"
                                ]
                            },
                            "symbol": {
                                "$id": "#/properties/metric_tags/items/anyOf/0/properties/symbol",
                                "type": "string",
                                "title": "The symbol schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "sysName"
                                ]
                            },
                            "tag": {
                                "$id": "#/properties/metric_tags/items/anyOf/0/properties/tag",
                                "type": "string",
                                "title": "The tag schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "snmp_host"
                                ]
                            }
                        },
                        "additionalProperties": True
                    }
                ]
            }
        }
    },
    "additionalProperties": True
})
