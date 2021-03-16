import React, { FC, ReactElement, useEffect } from 'react'
import { getPost, getSortedPostsData } from '../../src/lib/posts'
import { PostData } from '../../src/types/posts'
import { GetStaticPropsContext, GetStaticPropsResult } from 'next'
import marked from 'marked'
import Head from 'next/head'
import hljs from 'highlight.js'
import '../../node_modules/highlight.js/styles/monokai.css'
import '../../node_modules/highlight.js/lib/highlight'
import styles from '../../styles/Slug.module.css'
import { PageHeading } from '../../src/components/PageHeading'
import { Card, CardMedia, Typography } from '@material-ui/core'
import GitHubIcon from '@material-ui/icons/GitHub'
import TopicsDisplay from '../../src/components/TopicsDisplay'
import PreviewCard from '../../src/components/PreviewCard'
import { BASE_URL, NAME } from '../../src/types/constants'

type Props = { postData: PostData; nextPath: PostData }

const Slug: FC<Props> = ({ postData, nextPath }): ReactElement => {
  marked.setOptions({
    highlight: function (code) {
      return hljs.highlightAuto(code).value
    },
  })

  useEffect(() => {
    document.querySelectorAll('pre code').forEach((block: HTMLElement) => {
      hljs.highlightBlock(block)
    })
  }, [postData])

  return (
    <>
      <Head>
        <title>{postData.title}</title>
        <meta name="description" content={postData.description} />
        <meta property="article:published_time" content={`${postData.date}T10:00:00Z`} />
        <meta name="twitter:card" content="summary" />
        <meta name="twitter:description" content={postData.description} />
        <meta name="twitter:title" content={postData.title} />
        <meta name="twitter:image" content={`${BASE_URL}/small/${postData.id}.png`} />
        <meta property="og:type" content="article" />
        <meta property="og:title" content={postData.title} />
        <meta property="og:description" content={postData.description} />
        <meta property="og:url" content={`${BASE_URL}/blog/${postData.id}`} />
        <meta property="og:site_name" content={NAME} />
        <meta property="og:image" content={`${BASE_URL}/small/${postData.id}.png`} />
        <meta property="og:image:secure_url" content={`${BASE_URL}/small/${postData.id}.png`} />
      </Head>
      <div className={styles['text-content']}>
        <PageHeading title={postData.title} />
      </div>
      <div className={styles['image-container']}>
        <div className={styles.info}>
          <Typography variant="body1">
            {postData.date} — written by{' '}
            <a
              href="http://www.github.com/saiemgilani"
              target="_blank"
              rel="noreferrer"
              style={{
                display: 'inline-flex',
                alignItems: 'center',
              }}
            >
              Saiem Gilani <GitHubIcon fontSize="small" style={{ marginLeft: 10 }} />
            </a>
          </Typography>
          <TopicsDisplay topics={postData.topics} n={10} noMargin />
        </div>
      </div>
      <div className={styles['image-container']}>
        <Card className={styles.image}>
          <CardMedia>
            <img alt={postData.title} loading="lazy" src={`/small/${postData.id}.png`} />
          </CardMedia>
        </Card>
      </div>
      <div className={styles['post-container']} dangerouslySetInnerHTML={{ __html: marked(postData.content) }} />
      <div className={styles['post-container']} style={{ paddingTop: 50 }}>
        <hr />
        <Typography variant="h4" component="p" style={{ paddingBottom: 20 }}>
          Recommended
        </Typography>
        <PreviewCard post={nextPath} noMargin />
      </div>
    </>
  )
}

type StaticPaths = { paths: { params: { slug: string } }[]; fallback: boolean }

export const getStaticProps = async ({
  params: { slug },
}: GetStaticPropsContext<{ slug: string }>): Promise<
  GetStaticPropsResult<{
    postData: PostData
    nextPath: PostData
  }>
> => {
  const postData = getPost(slug, true)

  const paths = getSortedPostsData()

  const nextPath = !postData.recommended
    ? paths.reduce((prev, curr, i) => (curr.id === slug && i >= 1 ? paths[i - 1] : curr), paths[paths.length - 1])
    : paths.filter((p) => p.id === postData.recommended).pop()

  return {
    props: {
      postData,
      nextPath,
    },
  }
}

export const getStaticPaths = async (): Promise<StaticPaths> => {
  const paths = getSortedPostsData().map(({ id }) => ({
    params: {
      slug: id,
    },
  }))

  return {
    paths,
    fallback: false,
  }
}

export default Slug
