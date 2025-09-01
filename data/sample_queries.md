# 📝 Sample User Queries for Testing

এই ফাইলটি টেস্টিং এবং ডেমোর জন্য কিছু নমুনা ইউজার কোয়েরি ধারণ করে।

## ✅ Valid Queries

- "Plan a 3-day romantic trip to Paris focused on food and museums."
- "I want a cheap 1-day trip to Tokyo with street food and shopping."
- "Create a family-friendly itinerary for 2 days in Paris with kids."
- "I love nature — suggest a relaxed 3-day plan in Tokyo with parks and temples."
- "Plan a luxury trip to Paris for 4 days with fine dining and shopping."

## ❌ Edge Case Queries

- "Plan a trip to Mars for 5 days." → Should handle gracefully
- "I want to visit Paris in 0 days." → Validate days > 0
- "" → Empty input
- "What is the weather?" → Out of scope, but bot should respond politely

## 💡 Tips for Voiceflow Testing

- Use these in manual chat testing
- Check if the response is structured and includes:
  - Day-wise schedule
  - Practical tips
  - Realistic timing
  - Local recommendations
