import {Breadcrumb, Tag} from "antd";
import {GithubOutlined, SyncOutlined} from "@ant-design/icons";
import React from "react";

const PageTags = () => {
    return (
        <Breadcrumb
            style={{
                margin: '16px 0',
            }}
        >
            <Breadcrumb.Item>
                    <span className="project">
                            <span className="font">
                                <a href="https://github.com/LockGit/gochat" target="_blank">
                                    <GithubOutlined/> 源项目 LockGit/gochat
                                </a>
                            </span>
                    </span>
                <span style={{margin: "0 0 0 20px"}}>
                        <Tag icon={<SyncOutlined spin/>} color="processing">gochat</Tag>
                    </span>
            </Breadcrumb.Item>
        </Breadcrumb>
    )
}
export default PageTags;