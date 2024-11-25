লিনিয়ার রিগ্রেশন (Linear Regression) মেশিন লার্নিং-এ
লিনিয়ার রিগ্রেশন হলো মেশিন লার্নিংয়ের একটি সুপারভাইজড লার্নিং অ্যালগরিদম, যা নির্ভরশীল (dependent) এবং স্বাধীন (independent) ভেরিয়েবলের মধ্যে সম্পর্ক স্থাপন করতে সাহায্য করে। এটি প্রধানত ভবিষ্যদ্বাণী (prediction) এবং ডেটা মডেলিংয়ে ব্যবহৃত হয়।

লিনিয়ার রিগ্রেশনের ধারণা
লিনিয়ার রিগ্রেশনে আমরা একটি সরাসরি রেখা (Straight Line) দিয়ে ডেটা পয়েন্টগুলোকে যতটা সম্ভব ভালোভাবে ফিট করার চেষ্টা করি।

রেখাটির সমীকরণ হলো:

`𝑦
=
𝑚
𝑥
+
𝑐
`
y=mx+c
এখানে,

𝑦
y: নির্ভরশীল ভেরিয়েবল (Target/Output)
𝑥
x: স্বাধীন ভেরিয়েবল (Feature/Input)
𝑚
m: স্লোপ বা ঢাল (Coefficient)
𝑐
c: ইন্টারসেপ্ট বা শুরুর মান (Constant)
লিনিয়ার রিগ্রেশনের কাজের ধাপ
ডেটা সংগ্রহ ও প্রস্তুতি:

ডেটা সেট সংগ্রহ করা এবং সেটি পরিস্কার করা।
ইনপুট (Feature) এবং আউটপুট (Target) আলাদা করা।
সমীকরণের উপাদান নির্ধারণ:

স্লোপ (
𝑚
m) এবং ইন্টারসেপ্ট (
𝑐
c) এমনভাবে নির্ধারণ করা হয় যাতে প্রেডিকশন ও আসল ডেটার মধ্যে তফাৎ কম থাকে।
লস ফাংশন ব্যবহার:

মীন স্কয়ার্ড এরর (Mean Squared Error) ব্যবহার করা হয়। এটি প্রেডিকশনের ভুল পরিমাপ করে।
𝑀
𝑆
𝐸
=
1
𝑛
∑
𝑖
=
1
𝑛
(
𝑦
𝑖
−
𝑦
^
𝑖
)
2
MSE= 
n
1
​
  
i=1
∑
n
​
 (y 
i
​
 − 
y
^
​
  
i
​
 ) 
2
 
এখানে,
𝑦
^
𝑖
y
^
​
  
i
​
 : প্রেডিকশন
𝑦
𝑖
y 
i
​
 : আসল মান
𝑛
n: ডেটার সংখ্যা

অপ্টিমাইজেশন:

গ্রেডিয়েন্ট ডেসেন্ট (Gradient Descent) অ্যালগরিদম ব্যবহার করে 
𝑚
m এবং 
𝑐
c-এর মান আপডেট করা হয়, যাতে লস কমে।
লিনিয়ার রিগ্রেশনের প্রকারভেদ
সাধারণ লিনিয়ার রিগ্রেশন:

একাধিক ইনপুট ফিচার নেই। শুধু একটিমাত্র 
𝑥
x ভেরিয়েবলের ওপর ভিত্তি করে 
𝑦
y প্রেডিক্ট করে।
মাল্টিপল লিনিয়ার রিগ্রেশন:

একাধিক ইনপুট ফিচার থাকে। সমীকরণ হয়:
𝑦
=
𝑚
1
𝑥
1
+
𝑚
2
𝑥
2
+
.
.
.
+
𝑚
𝑛
𝑥
𝑛
+
𝑐
y=m 
1
​
 x 
1
​
 +m 
2
​
 x 
2
​
 +...+m 
n
​
 x 
n
​
 +c
লিনিয়ার রিগ্রেশনের উদাহরণ
ধরা যাক, একটি কোম্পানি প্রেডিক্ট করতে চায়, একজন কর্মীর অভিজ্ঞতার (Experience) ওপর ভিত্তি করে তার মাসিক বেতন (Salary) কত হবে।
ডেটা:

𝑥
x: কর্মীর অভিজ্ঞতা (বছরে)
𝑦
y: বেতন (টাকায়)
লিনিয়ার রিগ্রেশন মডেল অভিজ্ঞতার ওপর ভিত্তি করে একটি রেখা তৈরি করবে, যা ভবিষ্যতে কর্মীদের বেতন প্রেডিক্ট করতে সাহায্য করবে।

লিনিয়ার রিগ্রেশনের সুবিধা
সহজ এবং ব্যাখ্যা করা যায়।
অল্প ডেটা থাকা অবস্থায়ও ভালো কাজ করে।
ইন্টারপ্রিটেবল মডেল (কেন কোনো সিদ্ধান্ত নেওয়া হলো, তা ব্যাখ্যা করা যায়)।
লিনিয়ার রিগ্রেশনের সীমাবদ্ধতা
এটি শুধুমাত্র সরল সম্পর্ক (Linear Relationship) ধারণা করে। যদি সম্পর্ক নন-লিনিয়ার হয়, তাহলে এটি সঠিক প্রেডিকশন করতে পারে না।
আউটলায়ার (অস্বাভাবিক ডেটা পয়েন্ট) মডেলের সঠিকতা নষ্ট করতে পারে।
বড় ডেটাসেট বা জটিল সমস্যার জন্য এটি কার্যকর নয়।
উপসংহার
লিনিয়ার রিগ্রেশন সহজ এবং শক্তিশালী একটি মডেল, যা ছোট ডেটাসেট এবং সরল সম্পর্ক বিশ্লেষণে কার্যকর। তবে, জটিল পরিস্থিতিতে এটি অন্য অ্যালগরিদমের মতো ভালো পারফর্ম নাও করতে পারে।

আপনার যদি কোনো কোড বা বাস্তব উদাহরণ প্রয়োজন হয়, জানাবেন!