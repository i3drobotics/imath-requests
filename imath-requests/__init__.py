def part_create_json():
    part_json = {
      "timestamp": 1516193959559,
      "part_id": "Part1234",
      "source": "Camera_Control_PC_Garret",
      "part_data": [
        {
          "key": "steel_grade",
          "value": "Grade01"
        },
        {
          "key": "heat_number",
          "value": "C1234566"
        },
        {
          "key": "rolling_schedule",
          "value": "Schedule1"
        },
        {
          "key": "analysis",
          "value": [
            {
              "key": "C",
              "value": "0.2"
            },
            {
            "key": "Mn",
            "value": "0.02"
            }
          ]
        }
      ]
     }

    # Image meta data
# {
#  "part_id" : "Part1234",
#  "value_id" : "Camera1"
#  "source": "Camera_Control_PC_Garret",
#  "values" : [
#  { "value": "Part1234_1.1_2.2_1.jpg",
#  "timestamp": "1516193959559",
#  "position": [346.2,2],
#  "dimension" : [5.2,1],
#  "quality" : "1"
#  },
#  { "value": "Part1234_1.1_2.2_2.jpg",
#  "timestamp": "1516193959559",
#  "position": [246.2,5],
#  "dimension" : [1.7,4],
#  "quality" : "-1"
#  }
#  ],
#  "qualifying_metadata" : [
#  { "key": "key1",
#  "value": "value1"
#  },
#  { "key": "key2",
#  "value": "value2"
#  }
#  ]
# }


# ML result data
# {
#  "part_id": "Part1234",
#  "source": "Analysis System",
#  "value": "Part1234_1.1_2.2_1.jpg",
#  "timestamp": "1516193959559",
#  "failures": [
#  {
#  "id": 124355435321576
#  "failure": "4711",
#  "position": [
#  44.2,
#  17.4
#  ],
#  "dimension": [
# Page 8 of 10
#  5.2,
#  1
#  ],
#  "qualifying_metadata": [
#  {
#  "key": "xxx",
#  "value": "1"
#  },
#  {
#  "key": "yyy",
#  "value": "2"
#  }
#  ]
#  },
#  {
#  "id": 124355435321578
#  "failure": "4712",
#  "position": [
#  33.2,
#  3
#  ],
#  "dimension": [
#  2.3,
#  1.1
#  ],
#  "qualifying_metadata": [
#  {
#  "key": "xxx",
#  "value": "1"
#  },
#  {
#  "key": "yyy",
#  "value": "2"
#  }
#  ]
#  }
#  ]
# }

# # Create a new resource
# response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# # Update an existing resource
# requests.put('https://httpbin.org/put', data = {'key':'value'})
