import { Variants } from "framer-motion";
import { MDXRemoteSerializeResult } from "next-mdx-remote";
import React from "react";
import { IconType } from "react-icons/lib";
import { ReadTimeResults } from "reading-time";

/* Custom Animated Components types */
export type AnimatedTAGProps = {
  variants: Variants;
  className?: string;
  children: React.ReactNode;
  infinity?: boolean;
};

export type ProjectType = {
  id: string;
  name: string;
  coverImage: string;
  description: string;
  githubURL: string;
  previewURL?: string;
  tools?: string[];
  pinned?: boolean;
};

export type SkillType = {
  name: string;
  Icon: IconType;
};


export type SocialPlatform = {
  title: string;
  Icon: IconType;
  url: string;
};

export type UtilityType = {
  title: string;
  data: {
    name: string;
    description: string;
    Icon: IconType | JSX.Element;
    link: string;
  }[];
};

export type Utilities = {
  title: string;
  description: string;
  lastUpdate: string;
  data: UtilityType[];
};

export type Author = {
  name?: string
  picture?: string
}

export type FrontMatter = {
  slug: string;
  readingTime: ReadTimeResults;
  excerpt: string;
  title: string;
  author?: Author;
  date: string;
  keywords: string;
  image: string;
};

export type PostType = {
  meta: FrontMatter;
  source: MDXRemoteSerializeResult;
  tableOfContents: TableOfContents[];
};

export type TableOfContents = {
  level: number;
  heading: string;
};

export type SupportMe = {
  name: string;
  url: string;
  Icon: IconType;
};

export type FormInput = {
  to_name: string;
  first_name: string;
  last_name: string;
  email: string;
  subject: string;
  message: string;
};


export type GithubRepo = {
  stargazers_count: number;
  fork: boolean;
  forks_count: number;
};

export type PageData = {
  title: string;
  description: string;
  image: string;
  keywords: string;
};

export type PageMeta = {
  home: PageData;
  packages: PageData;
  stats: PageData;
  blog: PageData;
  bookmark: PageData;
  projects: PageData;
  about: PageData;
  privacy: PageData;
  snippets: PageData;
};

export type Snippet = {
  slug: string;
  title: string;
  date: string;
  excerpt: string;
  image: string;
};


export type subscriptionURL = {
  url: string;
};

export type mongoClient = {
  client: any;
  db: any;
};