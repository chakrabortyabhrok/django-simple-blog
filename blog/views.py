from django.http import HttpResponse
from django.shortcuts import render
posts = [
    {
        "title": "Morning Yoga for Beginners",
        "slug": "morning-yoga-beginners",
        "excerpt": "Start your day with simple yoga poses to boost energy and focus.",
        "date": "2026-04-10",
        "content": """Yoga in the morning is a game-changer for mental clarity. By starting your day with gentle movement, you wake up your nervous system without the jarring effect of a loud alarm or immediate caffeine. 

        Focus on child's pose, cat-cow stretches, and a basic downward dog. These poses help decompress the spine after a night of sleep. Remember, it's not about being flexible; it's about being present. Spending just ten minutes on your mat can set a positive tone for the next twelve hours of your day."""
    },
    {
        "title": "How to Bake Perfect Chocolate Chip Cookies",
        "slug": "bake-chocolate-chip-cookies",
        "excerpt": "A foolproof recipe for soft, chewy cookies every time.",

        "date": "2026-04-09",
        "content": """The secret to a perfect cookie isn't just the sugar; it's the temperature of your butter. Using room-temperature butter allows it to cream properly with the sugars, creating tiny air pockets that lead to a soft texture.

        Always chill your dough for at least 30 minutes before baking to prevent excessive spreading. Don't forget a pinch of sea salt on top! The contrast between the sweet chocolate and the salt brings out the depth of the vanilla and brown sugar in the dough."""
    },
    {
        "title": "Top 5 Productivity Apps for Students",
        "slug": "productivity-apps-students",
        "excerpt": "Discover apps that help you study smarter and stay organized.",
        "date": "2026-04-08",
        "content": """Staying organized in college is a massive challenge. Thankfully, digital tools have made it easier to keep track of deadlines and notes. Notion remains a top choice for its 'all-in-one' workspace feel, allowing you to link databases and class schedules.

        For focus, apps like Forest use gamification to keep you off your phone. If you struggle with the Pomodoro technique, simple timers like Be Focused can help break your study sessions into manageable chunks. Remember, the best app is the one you actually use consistently."""
    },
    {
        "title": "Urban Gardening on a Balcony",
        "slug": "urban-gardening-balcony",
        "excerpt": "Turn your small space into a green oasis with these tips.",
        "date": "2026-04-07",
        "content": """You don't need a backyard to be a gardener. Balcony gardening is all about maximizing vertical space. Use hanging planters and tiered shelving to give your plants room to breathe and catch the sunlight.

        When selecting plants, consider the 'microclimate' of your balcony. Does it get harsh afternoon sun, or is it mostly shaded? Herbs like basil, mint, and rosemary are incredibly resilient and perfect for beginners. Just make sure your pots have proper drainage to prevent root rot."""
    },
    {
        "title": "Easy Weeknight Pasta Recipes",
        "slug": "easy-pasta-recipes",
        "excerpt": "Delicious pasta dishes ready in under 30 minutes.",
        "date": "2026-04-05",
        "content": """Weeknight cooking should be efficient but never boring. A classic Aglio e Olio requires only garlic, olive oil, chili flakes, and parsley, yet it tastes like a restaurant-quality meal. 

        The trick is to use high-quality olive oil and to save a cup of the starchy pasta water. When you toss the pasta with the oil and water, it creates a silky emulsion that coats every strand. It's fast, cheap, and incredibly satisfying after a long day at work."""
    },
    {
        "title": "How to Stay Fit While Working from Home",
        "slug": "stay-fit-remote-work",
        "excerpt": "Simple exercises and habits to stay active at home.",
        "date": "2026-04-04",
        "content": """The biggest enemy of remote work fitness is the 'sedentary slump.' When your commute is only ten steps to the kitchen, your step count plummets. To counter this, implement a 'fake commute'—a 15-minute walk before and after work.

        Invest in a standing desk or simply use 'exercise snacks.' These are 2-minute bursts of movement, like air squats or wall pushes, done every hour. This keeps your metabolism active and prevents the dreaded lower back pain associated with poor desk posture."""
    },
    {
        "title": "Digital Minimalism: Declutter Your Phone",
        "slug": "digital-minimalism-phone",
        "excerpt": "Reduce screen time by organizing and simplifying your device.",
        "date": "2026-04-03",
        "content": """Your phone is a tool, not a master. Digital minimalism is the practice of intentionally choosing which apps serve you and which ones just steal your time. Start by deleting any app you haven't opened in the last thirty days.

        Next, turn off all non-human notifications. If it's not a message from a real person, you probably don't need to see it immediately. By cleaning up your home screen and keeping only 'utility' apps visible, you reduce the urge to mindlessly scroll through social media feeds."""
    },
    {
        "title": "Travel Tips for Solo Adventurers",
        "slug": "solo-travel-tips",
        "excerpt": "Stay safe and make the most of your solo journey.",
        "date": "2026-04-02",
        "content": """Solo travel is the ultimate form of self-discovery. Without a companion to lean on, you're forced to interact with the world on your own terms. Safety should be your priority: always share your itinerary with someone back home and keep a backup of your documents online.

        Embrace the freedom to change your plans at a moment's notice. If you love a city, stay longer. If a museum doesn't interest you, skip it. Learning to enjoy your own company at a dinner table or a park bench is a superpower that stays with you long after the trip ends."""
    },
    {
        "title": "How I Built My First Full-Stack Project in 11 Weeks",
        "slug": "first-fullstack-project",
        "excerpt": "My personal journey following this exact roadmap.",
        "date": "2026-04-07",
        "content": """Building a full-stack application felt impossible when I started. The journey from 'Hello World' to a functioning database-driven site was a rollercoaster of syntax errors and 'Aha!' moments. 

        The first three weeks were dedicated solely to HTML and CSS layouts. Then came the deep dive into Python and Django. Learning how to connect a front-end form to a back-end model was the most challenging part, but seeing the data persist in the database for the first time made it all worth it. My advice? Don't try to learn everything at once; focus on building one feature at a time."""
    }
]

def home_page(request):
    return render(request, 'blog/home.html')

def about_page(request):
    return render(request, 'blog/about.html')

def blog_list(request):
    return render(request, 'blog/post_list.html', {'posts': posts})

def  post_detail(request, slug):
    post = next((p for p in posts if p['slug'] == slug), None)
    if post is None:
        return HttpResponse("404 - Post not found", status=404)
    return render(request, 'blog/post_detail.html', {'post' : post})