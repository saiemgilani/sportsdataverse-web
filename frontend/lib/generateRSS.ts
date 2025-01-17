import { writeFileSync } from "fs";
import MDXContent from "./MDXContent";
import RSS from "rss";

export default async function getRSS() {
  const siteURL = "https://sportsdataverse.org";
  const allBlogs = new MDXContent("posts").getAllPosts();

  // Create a new RSS object
  const feed = new RSS({
    title: "SportsDataverse",
    description: `We've been creating packages for sports data and analytics purposes, mostly in Python, R, and Node.js.`,
    site_url: siteURL,
    feed_url: `${siteURL}/feed.xml`,
    language: "en",
    pubDate: new Date(),
    copyright: `All rights reserved ${new Date().getFullYear()}, SportsDataverse`,
  });

  // Add all blog posts to the RSS feed
  allBlogs?.map((post) => {
    feed.item({
      title: post!.title,
      url: `${siteURL}/blog/${post?.slug}`,
      date: post!.date,
      description: post!.excerpt,
    });
  });

  // Write the RSS feed to a file
  writeFileSync("./public/feed.xml", feed.xml({ indent: true }));
}
