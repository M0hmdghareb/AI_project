
from main import generate_title, generate_description, search_image
def generate_schema(user_text):
  # Construct the state array
  initial_state = {
      'navbar': {
          'imgUrl': search_image(f"i need icon for  {user_text} which used as navbar icon"),
          "links": ["home", "pages", "services", "projects", "blog", "contact"],
      },
      'hero': {
          'title': generate_title( f"Suggest a title for a website about {user_text}"),
          'description': generate_description(f"Create a brief description for a website about {user_text}"),
          'imgUrl': search_image(f"i need image which used as wallpaber for website about  {user_text}"),
          'buttonText': "Get Started",
          'icon':"https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg", 
      },
      'services': {
          'blocks': [
        {
          'icon': search_image(f" vector icon representing a service one {user_text}"),
          'title': generate_title( f"Suggest a title for a service related to {user_text}"),
          'description': generate_description(f"Create a brief description for a service related to {user_text}"),
        },
        {
          'icon': search_image(f"vector icon representing a service two {user_text}"),
          'title': generate_title( f" Suggest another title for a service related to {user_text}"),
          'description':  generate_description(f"Create another brief description for a service related to  {user_text}"),
        },
        {
          'icon': search_image(f"vector icon representing a service three  {user_text}"),
          'title': generate_title( f" Suggest one more title for a service related to {user_text}"),
          'description':  generate_description(f"Create one more brief description for a service related to {user_text}"),
        },
      ],
    },
    'feature': {
      'title': generate_title(f"Suggest a title for a feature related to {user_text}"), 
      'description': generate_description(f"Create a brief description for a feature related to{user_text}"),
      'phone': '012345678', 
      'buttonText': 'Get Free Estimate',

      'icons': [
        {
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813236/templates/template_one/Call_gqvv4l.svg",
        },
        {
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg" ,
        }
      ],

      'test': [
        {
          'subTest': [
          "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813236/templates/template_one/Call_gqvv4l.svg",
          "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
          "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
          ]
        }
      ],

      'imgUrl': search_image(f"i need image describe the  {user_text} as feature")
    },
    'testimonials': {
    'title': "What the People Thinks About Us",
  
    'cards': [
      {
        'name': generate_title("generate the name of client 1 that use our services"),
        'location': generate_title('genrate the location 2 of client that use our services'),
        'imgUrl': search_image("https://res.cloudinary.com/duc04fwdb/image/upload/v1701808853/templates/template_one/Photo_1_zsyklb.jpg"),  
        'opinion': generate_description(f" generate a brief description for client that use our services about {user_text}"),
      },
      {
        'name': generate_title("generate the name of client 2 that use our services"),
        'location': generate_title('genrate the location 1 of client that use our services'),
        'imgUrl': search_image("https://res.cloudinary.com/duc04fwdb/image/upload/v1701808853/templates/template_one/Photo_1_zsyklb.jpg"),  
        'opinion': generate_description(f" generate a brief description for client that use our services about {user_text}"),
      },
      {
        'name': generate_title("generate the name of client 3 that use our services"),
        'location': generate_title('genrate the location 3 of client that use our services'),
        'imgUrl': search_image("https://res.cloudinary.com/duc04fwdb/image/upload/v1701808853/templates/template_one/Photo_1_zsyklb.jpg"),  
        'opinion': generate_description(f" generate a brief description for client that use our services about {user_text}"),
      }
      ]
  },
    'logos' : {

    'companies': [
      {'imgUrl': search_image(f"logo 1 for company which related to {user_text}  ")},
      {'imgUrl': search_image(f"logo 2 for company which related to {user_text}  ")},
      {'imgUrl': search_image(f"logo 3 for company which related to {user_text}  ")},
      {'imgUrl': search_image(f"logo 4 for company which related to {user_text}  ")},
      {'imgUrl': search_image(f"logo 5 for company which related to {user_text}  ")}
      ]   
    },
    'projects':{

      'title': generate_title(f"Suggest a title for a section about projects related to {user_text}"),
      'description': generate_description(f"Write a brief description for the projects section of a {user_text} website"),
      
      'cards': [
          {
          'imgUrl': search_image(f"i need image which used for website about  {user_text} to represent the name of first project it's can do" ),
          'title': generate_title(f"Suggest a title for a project name related to  {user_text}"),
          'description': generate_description(f"Create brief description for a project related to {user_text}"),
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg" ,
          },
          {
          'imgUrl': search_image(f"i need image which used for website about  {user_text} to represent the name of the secand project it's can do"),
          'title': generate_title(f"Suggest another title for a project name related to  {user_text}"),
          'description': generate_description(f"Create another brief description for a project related to {user_text}"),
          'icon':"https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg" ,
          },
          {
          'imgUrl': search_image(f"i need image which used for website about  {user_text} to represent the name of the third project it's can do"),
          'title': generate_title(f"Suggest one more title for a project name related to  {user_text}"),
          'description': generate_description(f"Create one more brief description for a project related to {user_text}"),
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg", 
          },
          {
          'imgUrl': search_image(f"i need image which used for website about  {user_text} to represent the name of fourth project it's can do"),
          'title': generate_title(f"Suggest second more title for a project name related to  {user_text}"),
          'description': generate_description(f"Create second more brief description for a project related to {user_text}"),
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg" ,
          }
      ]

    },
      'statistic': {
      'statistics': [
        {
          'title': "Years Of Experience",
          'value': "12",
        },
        {
          'title': "Success Projects",
          'value': "85",
        },
        {
          'title': "Active Projects",
          'value': "15",
        },
        {
          'title': "Happy Customers",
          'value': "95",
        },
      ],
    },
    'items' : {

    'title': "Articles & News",
    'description': "It is a long established fact that a reader will be distracted by the of readable content of a page when lookings at its layouts the points of using.",


    'cards': [
      {
        'title': generate_description(f"Generate a brief article description related to {user_text}"),
        'description': "26 December,2022 ",
        'imgUrl': search_image(f"i need image matche with first artical name related to website {user_text}"),
        'icon':"https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
        'caption': generate_title(f"Generate a creative article title related to {user_text}"),
      },
      {
        'title': generate_description(f"Generate another brief article description related to {user_text}"),
        'description':"10 December,2022 ",
        'imgUrl': search_image(f"i need image matche with secand artical name related to website {user_text}"),
        'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
        'caption': generate_title(f"Generate another creative article title related to {user_text}")
      },
      {
        'title': generate_description(f"Generate one more brief article description related to {user_text}"),
        'description': "1 December,2022 ",
        'imgUrl': search_image(f"i need image matche with third artical name related to website {user_text}"),
        'icon':"https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
        'caption': generate_title(f"Generate one more creative article title related to {user_text}")
      }
    ]

  },
  'team': {
      'title': "Our Team Members",
      'cards': [
        {
          'id': "262024507",
          'name': "Nattasha",
          'location': "Design, Australia",
          'imgUrl': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
          'mediaIcons': [
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
              'url': "https://facebook.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
              'url': "https://x.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
              'url': "https://linkedin.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
              'url': "https://instagram.com",
            },
          ],
          'email': "julie@email.com",
        },
        {
          'id': "262024508",
          'name': "Julie",
          'location': "Design, Australia",
          'imgUrl': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
          'mediaIcons': [
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
              'url': "https://facebook.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
              'url': "https://x.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
              'url': "https://linkedin.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
              'url': "https://instagram.com",
            },
          ],
          'email': "julie@email.com",
        },
        {
          'id': "262024509",
          'name': "Alex",
          'location': "Design, Australia",
          'imgUrl': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
          'mediaIcons': [
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
              'url': "https://facebook.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
              'url': "https://x.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
              'url': "https://linkedin.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
              'url': "https://instagram.com",
            },
          ],
          'email': "julie@email.com",
        },
        {
          'name': "John",
          'location': "Design, Australia",
          'imgUrl': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
          'mediaIcons': [
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
              'url': "https://facebook.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
              'url': "https://x.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
              'url': "https://linkedin.com",
            },
            {
              'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
              'url': "https://instagram.com",
            },
          ],
          'email': "julie@email.com",
        },
      ],
    },
    'pricing': {
      'title': "Pricing & Plan",
      'description': "Home / Priceing",
      'blocks': [
        {
          'plan': "Design advices",
          'price': "29",
          'timeUnit': "/month",
          'moneyUnit': "$",
          'features': ["General living space advices", "Renovation advices", "Interior design advices", "Furniture reorganization", "Up to 5 hours meetings"],
          'buttonText': "Get Started",
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
        },
        {
          'plan': "Complete interior",
          'price': "39",
          'timeUnit': "/month",
          'moneyUnit': "$",
          'PopularPlan': "Most Popular Plans",
          'features': ["Complete home redesign", "Interior and exterior works", "Modular interior planning", "Kitchen design", "Garages organization"],
          'buttonText': "Get Started",
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
        },
        {
          'plan': "Furniture design",
          'price': "59",
          'timeUnit': "/month",
          'moneyUnit': "$",
          'features': ["Furniture for living room", "Furniture refurbishment", "Sofas and armchairs", "Tables and chairs", "Kitchens"],
          'buttonText': "Get Started",
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
        },
      ],
    },
    'cta': {
      'title': "Wanna join us?",
      'description': "It is a long established fact  will be distracted.",
      'buttonText': "Contact With Us",
      'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
    },
    'footer': {
      'imgUrl': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
      'description': "It is a long established fact that a reader will be distracted lookings.",
      'mediaIcons': [
        {
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
          'url': "https://facebook.com",
        },
        {
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
          'url': "https://x.com",
        },
        {
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
          'url': "https://linkedin.com",
        },
        {
          'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
          'url': "https://instagram.com",
        },
      ],
      'items': [
        {
          'title': "services",
          'links': ["Kitchan,", "Living Area,", "Bathroom,", "Dinning Hall,", "Bedroom"],
        },
        {
          'title': "section",
          'links': ["About Us", " Projects", "Our Team", "Contact Us", "Services"],
        },
      ],
      'contact': {
        'title': "contact",
        'location': "55 East Birchwood Ave. Brooklyn, New York 11201",
        'email': "contact@interno.com",
        'phone': "(123) 125-858",
      },
    'colors': {
      'templateColors': ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"],
    },

    }, 
  }
  return initial_state


# the test sample ?
#print(generate_schema("flower"))