<template>
    <div style="display: flex;">
        <div class="file-section">
            <div style="width: 95%;margin-top: 20px;margin-left: 10px;">
                <div style="display: flex;align-items: center;">
                    <bk-icon type="arrows-left-shape" @click="backDir" style="cursor: pointer;"></bk-icon>
                    <bk-input :clearable="true" v-model="filePath"
                        @enter="handleSearchFile"
                        :placeholder="'请输入文件夹路径：'"
                        behavior="simplicity">
                    </bk-input>
                    <bk-icon type="arrows-down-shape" @click="handleSearchFile" style="cursor: pointer;"></bk-icon>
                </div>
                <div style="margin-top: 10px;">
                    <bk-input type="text" v-model="searchWord" placeholder="search..." @enter="handleSearch"></bk-input>
                </div>
                <transition name="bk-slide-fade-down">
                    <div style="margin-top: 10px;" v-show="fadeShowDir">
                        <bk-tree
                            ref="tree1"
                            :data="treeListOne"
                            :multiple="true"
                            :node-key="'id'"
                            :has-border="true"
                            :tpl="tpl"
                            @on-click="nodeClickOne"
                            @on-check="nodeCheckTwo"
                            @on-expanded="nodeExpandedOne">
                        </bk-tree>
                    </div>
                </transition>
            </div>
        </div>
        <div class="edit-section">
            <transition name="bk-slide-fade-left">
                <div style="margin-left: 40px;width: 500px;margin-top: 20px;"
                    v-show="musicInfo.title && checkedIds.length === 0">
                    <div style="width: 100%;display: flex;">
                        <bk-button :theme="'success'" :loading="isLoading" @click="handleClick" class="mr10"
                            style="width: 50%;">
                            保存信息
                        </bk-button>
                        <bk-select
                            :disabled="false"
                            :clearable="false"
                            v-model="resource"
                            style="width: 200px;"
                            ext-cls="select-custom"
                            ext-popover-cls="select-popover-custom">
                            <bk-option v-for="option in resourceList"
                                :key="option.id"
                                :id="option.id"
                                :name="option.name">
                            </bk-option>
                        </bk-select>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;margin-top: 10px;">
                        <div class="label1" v-bk-tooltips="'变量名:${title}'">标题：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfo.title"></bk-input>
                        </div>
                        <div>
                            <bk-icon type="arrows-right-shape" @click="toggleLock('title')"
                                style="cursor: pointer;color: #64c864;margin-left: 20px;"></bk-icon>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1" v-bk-tooltips="'变量名:${filename}'">文件名：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfo.filename"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1" v-bk-tooltips="'变量名:${artist}'">艺术家：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfo.artist"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1" v-bk-tooltips="'变量名:${album}'">专辑：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfo.album"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">风格：</div>
                        <div style="width: 70%;">
                            <bk-select
                                :disabled="false"
                                v-model="musicInfo.genre"
                                style="width: 250px;background: #fff;"
                                ext-cls="select-custom"
                                ext-popover-cls="select-popover-custom"
                                :placeholder="'请选择歌曲风格'"
                                searchable>
                                <bk-option v-for="option in genreList"
                                    :key="option.id"
                                    :id="option.id"
                                    :name="option.name">
                                </bk-option>
                            </bk-select>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">年份：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfo.year"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;flex-direction: column;">
                        <div style="display: flex;">
                            <div class="label1">歌词：</div>
                            <div style="width: 70%;">
                                <bk-input :clearable="true" v-model="musicInfo.lyrics" type="textarea" :rows="15"
                                ></bk-input>
                            </div>
                        </div>
                        <div style="display: flex;margin-top: 10px;">
                            <div class="label1">保存歌词lrc：</div>
                            <bk-switcher v-model="musicInfo.is_save_lyrics_file"></bk-switcher>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">描述：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfo.comment" type="textarea"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">专辑封面：</div>
                        <div style="width: 70%;" v-if="reloadImg">
                            <div v-if="musicInfo.album_img">
                                <bk-image fit="contain" :src="musicInfo.album_img" style="width: 128px;"></bk-image>
                            </div>
                            <div v-else>
                                <bk-image fit="contain" :src="musicInfo.artwork" style="width: 128px;"></bk-image>
                            </div>
                        </div>
                    </div>
                </div>
            </transition>
            <transition name="bk-slide-fade-left">
                <div style="margin-left: 40px;width: 500px;margin-top: 20px;" v-show="checkedIds.length > 0">
                    <div style="width: 100%;display: flex;">
                        <bk-button :theme="'success'" :loading="isLoading" @click="handleBatch" class="mr10"
                            style="width: 50%;">
                            手动批量修改
                        </bk-button>
                        <bk-button :theme="'success'" :loading="isLoading"
                            @click="exampleSetting1.primary.visible = true" class="mr10"
                            style="width: 50%;">
                            自动批量修改
                        </bk-button>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;margin-top: 10px;">
                        <div class="label1" v-bk-tooltips="'变量名:${title}'">标题：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfoManual.title"></bk-input>
                        </div>
                        <div>
                            <bk-icon type="arrows-right-circle" @click="toggleLock('title')"
                                style="cursor: pointer;font-size: 22px;color: #64c864;margin-left: 10px;"></bk-icon>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1" v-bk-tooltips="'变量名:${filename}'">文件名：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfoManual.filename"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1" v-bk-tooltips="'变量名:${artist}'">艺术家：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfoManual.artist"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1" v-bk-tooltips="'变量名:${album}'">专辑：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfoManual.album"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">风格：</div>
                        <div style="width: 70%;">
                            <bk-select
                                :disabled="false"
                                v-model="musicInfoManual.genre"
                                style="width: 250px;background: #fff;"
                                ext-cls="select-custom"
                                ext-popover-cls="select-popover-custom"
                                :placeholder="'请选择歌曲风格'"
                                searchable>
                                <bk-option v-for="option in genreList"
                                    :key="option.id"
                                    :id="option.id"
                                    :name="option.name">
                                </bk-option>
                            </bk-select>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">年份：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfoManual.year"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;flex-direction: column;">
                        <div style="display: flex;">
                            <div class="label1">歌词：</div>
                            <div style="width: 70%;">
                                <bk-input :clearable="true" v-model="musicInfoManual.lyrics" type="textarea" :rows="15"
                                ></bk-input>
                            </div>
                        </div>
                        <div style="display: flex;margin-top: 10px;">
                            <div class="label1">保存歌词lrc：</div>
                            <bk-switcher v-model="musicInfoManual.is_save_lyrics_file"></bk-switcher>
                        </div>
                    </div>

                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">描述：</div>
                        <div style="width: 70%;">
                            <bk-input :clearable="true" v-model="musicInfoManual.comment" type="textarea"></bk-input>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 10px;align-items: center;">
                        <div class="label1">专辑封面：</div>
                        <div style="width: 70%;">
                            <div v-if="musicInfoManual.album_img">
                                <bk-image fit="contain" :src="musicInfoManual.album_img" style="width: 128px;"
                                    v-if="reloadImg"></bk-image>
                            </div>
                            <div v-if="musicInfoManual.artwork">
                                <bk-image fit="contain" :src="musicInfoManual.artwork" style="width: 128px;"
                                    v-if="!musicInfoManual.album_img"></bk-image>
                            </div>
                        </div>
                    </div>
                </div>
            </transition>
        </div>
        <div class="resource-section">
            <transition name="bk-slide-fade-left">
                <div
                    style="display: flex;flex-direction: column;margin-top: 20px;flex: 1;margin-right: 20px;margin-left: 20px;"
                    v-show="fadeShowDetail">
                    <div v-if="SongList.length === 0">
                        <span style="margin-left: 30%;margin-top: 30%;">暂无歌曲信息</span>
                    </div>
                    <div v-else>
                        <div class="parent">
                            <div class="title2">应用</div>
                            <div class="title2">封面</div>
                            <div class="title2">歌曲名</div>
                            <div class="title2">歌手</div>
                            <div class="title2">专辑</div>
                            <div class="title2">歌词</div>
                            <div class="title2">年份</div>
                        </div>
                        <div v-for="(item,index) in SongList" :key="index" style="margin-bottom: 10px;" class="parent">
                            <bk-icon type="arrows-left-shape" @click="copyAll(item)"
                                style="margin-right: 5px;cursor: pointer;"></bk-icon>
                            <bk-image fit="contain" :src="item.album_img"
                                style="width: 64px;cursor: pointer;"
                                @click="handleCopy('album_img',item.album_img)">
                            </bk-image>
                            <div @click="handleCopy('title',item.name)" class="music-item">
                                {{
                                    item.name
                                }}
                            </div>
                            <div @click="handleCopy('artist',item.artist)" class="music-item">
                                {{ item.artist }}
                            </div>
                            <div @click="handleCopy('album',item.album)" class="music-item">
                                {{
                                    item.album
                                }}
                            </div>
                            <div @click="handleCopy('lyric',item.id)" class="music-item">加载歌词</div>
                            <div @click="handleCopy('year',item.year)" class="music-item">
                                {{
                                    item.year
                                }}
                            </div>
                            <bk-divider></bk-divider>
                            <bk-divider></bk-divider>
                            <bk-divider></bk-divider>
                            <bk-divider></bk-divider>
                            <bk-divider></bk-divider>
                            <bk-divider></bk-divider>
                            <bk-divider></bk-divider>
                        </div>
                    </div>
                </div>
            </transition>
            <div v-show="!fadeShowDetail" style="width: 90%;height: 90%; margin: 50px 20px 20px 50px;">
                <bk-image fit="contain" :src="'/static/dist/img/music_null-cutout.png'"
                    style="width: 100%;height: 98%;"></bk-image>
            </div>
        </div>
        <bk-dialog v-model="exampleSetting1.primary.visible"
            theme="primary"
            :mask-close="false"
            @confirm="handleBatchAuto"
            :header-position="exampleSetting1.primary.headerPosition"
            title="自动批量修改">
            <p>宽松模式: 只根据标题匹配元数据, 可能存在同名或翻唱歌曲。</p>
            <p>严格模式: 根据标题和歌手或标题和专辑匹配元数据, 准确性更高。</p>
            <bk-radio-group v-model="selectAutoMode">
                <bk-radio-button value="simple">
                    宽松模式
                </bk-radio-button>
                <bk-radio-button value="hard">
                    严格模式
                </bk-radio-button>
            </bk-radio-group>
            <div>音乐源顺序</div>
            <bk-select style="width: 250px;"
                searchable
                multiple
                show-select-all
                v-model="sourceList">
                <bk-option v-for="option in resourceList"
                    :key="option.id"
                    :id="option.id"
                    :name="option.name">
                </bk-option>
            </bk-select>
        </bk-dialog>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                searchWord: '',
                treeListOne: [],
                filePath: '/app/media/',
                fullPath: '',
                fileName: '',
                resource: 'netease',
                resourceList: [
                    {id: 'acoustid', name: '音乐指纹识别'},
                    {id: 'netease', name: '网易云音乐'},
                    {id: 'migu', name: '咪咕音乐'},
                    {id: 'qmusic', name: 'QQ音乐'},
                    {id: 'kugou', name: '酷狗音乐'},
                    {id: 'kuwo', name: '酷我音乐'}
                ],
                baseMusicInfo: {
                    'genre': '流行',
                    'is_save_lyrics_file': false
                },
                musicInfo: {
                    'genre': '流行',
                    'is_save_lyrics_file': false
                },
                musicInfoManual: {
                    'genre': '流行',
                    'is_save_lyrics_file': false
                },
                fadeShowDir: false,
                fadeShowDetail: false,
                isLoading: false,
                SongList: [],
                reloadImg: true,
                genreList: [
                    {'id': '流行', name: '流行'},
                    {'id': '摇滚', name: '摇滚'},
                    {'id': '说唱', name: '说唱'},
                    {'id': '民谣', name: '民谣'},
                    {'id': '电子', name: '电子'},
                    {'id': '爵士', name: '爵士'},
                    {'id': '纯音乐', name: '纯音乐'},
                    {'id': '金属', name: '金属'},
                    {'id': '世界音乐', name: '世界音乐'},
                    {'id': '新世纪', name: '新世纪'},
                    {'id': '古典', name: '古典'},
                    {'id': '独立', name: '独立'},
                    {'id': '氛围音乐', name: '氛围音乐'}
                ],
                checkedIds: [],
                checkedData: [],
                selectAutoMode: 'hard',
                sourceList: [],
                exampleSetting1: {
                    primary: {
                        visible: false,
                        headerPosition: 'left'
                    }
                }
            }
        },
        created() {
            this.handleSearchFile()
        },
        methods: {
            tpl(node, ctx) {
                // 如果在某些情况下 h 不能自动注入而报错，需将 h 参数写上；一般来说 h 默认是第一参数，但是现在改为第一参数会导致已经使用的用户都需要修改，所以先放在最后。
                // 如果 h 能自动注入则可以忽略 h 参数，无需写上，否则 h 参数会重复。
                const titleClass = node.selected ? 'node-title node-selected' : 'node-title ' + node.state
                console.log(node, titleClass)
                return <span>
                    <span class={titleClass} domPropsInnerHTML={node.title.slice(0, 30)}
                        onClick={() => {
                            this.nodeClickOne(node)
                        }} v-bk-tooltips={node.title}>
                    </span>
                </span>
            },
            backDir() {
                this.filePath = this.backPath(this.filePath)
                this.handleSearchFile()
            },
            backPath(path) {
                // 使用正则表达式匹配最后一个斜杠及其后面的内容
                const regex = /\/([^\/]+)\/?$/
                const match = regex.exec(path)

                // 如果匹配到了最后一个斜杠及其后面的内容
                if (match) {
                    // 截取掉最后一个斜杠及其后面的内容
                    const parentPath = path.slice(0, match.index)

                    // 返回回退后的路径
                    return parentPath
                }

                // 如果没有匹配到最后一个斜杠及其后面的内容，则返回原始路径
                return path
            },
            nodeClickOne(node) {
                if (node.icon === 'icon-folder') {
                    this.filePath = this.filePath + '/' + node.name
                    this.handleSearchFile()
                } else {
                    if (node.children && node.children.length > 0) {
                        return
                    }
                    this.musicInfo = this.baseMusicInfo
                    this.fileName = node.name
                    this.fullPath = this.filePath + '/' + node.name
                    this.$api.Task.musicId3({'file_path': this.filePath, 'file_name': node.name}).then((res) => {
                        console.log(res)
                        this.musicInfo = res.data
                        this.musicInfo.is_save_lyrics_file = false
                    })
                }
            },
            // checkbox
            nodeCheckTwo(node, checked) {
                console.log(node, checked)
                if (checked) {
                    this.musicInfo = this.baseMusicInfo
                    if (node.children && node.children.length > 0) {
                        this.checkedData = []
                        this.checkedIds = []
                        node.children.forEach(el => {
                            this.checkedData.push({
                                checked: el.checked,
                                icon: el.icon,
                                id: el.id,
                                name: el.name,
                                title: el.title
                            })
                            this.checkedIds.push(el.id)
                        })
                    } else {
                        this.checkedData.push({
                            checked: node.checked,
                            icon: node.icon,
                            id: node.id,
                            name: node.name,
                            title: node.title
                        })
                        this.checkedIds.push(node.id)
                    }
                } else {
                    if (node.children && node.children.length > 0) {
                        this.checkedData = []
                        this.checkedIds = []
                    } else {
                        const index = this.checkedIds.indexOf(node.id)
                        if (index !== -1) {
                            this.checkedData.splice(index, 1)
                            this.checkedIds.splice(index, 1)
                        }
                    }
                }
                console.log(this.checkedIds)
            },
            handleCopy(k, v) {
                if (k === 'lyric') {
                    this.$api.Task.fetchLyric({'song_id': v, 'resource': this.resource}).then((res) => {
                        console.log(res)
                        if (res.result) {
                            this.musicInfo['lyrics'] = res.data
                        } else {
                            this.$cwMessage('未找到歌词', 'error')
                        }
                    })
                } else if (k === 'album_img') {
                    this.musicInfo[k] = v
                    this.reloadImg = false
                    this.$nextTick(() => {
                        this.reloadImg = true
                    })
                } else {
                    this.musicInfo[k] = v
                }
            },
            copyAll(item) {
                this.handleCopy('title', item.name)
                this.handleCopy('year', item.year)
                this.handleCopy('lyric', item.id)
                this.handleCopy('album', item.album)
                this.handleCopy('artist', item.artist)
                this.handleCopy('album_img', item.album_img)
            },
            nodeExpandedOne(node, expanded) {
            },
            // 查询网易云接口
            toggleLock(mode) {
                if (mode === 'title') {
                    if (!this.musicInfo.title) {
                        this.$cwMessage('标题不能为空', 'error')
                        return
                    }
                    this.fadeShowDetail = false
                    this.$api.Task.fetchId3Title({
                        title: this.musicInfo.title,
                        resource: this.resource,
                        full_path: this.fullPath
                    }).then((res) => {
                        this.fadeShowDetail = true
                        this.SongList = res.data
                    })
                }
            },
            // 文件目录
            handleSearchFile() {
                this.fadeShowDir = false
                this.checkedData = []
                this.checkedIds = []
                this.$api.Task.fileList({'file_path': this.filePath}).then((res) => {
                    if (res.result) {
                        this.treeListOne = res.data
                        this.fadeShowDir = true
                    }
                })
            },
            // 过滤搜索
            handleSearch() {
                this.$refs.tree1.searchNode(this.searchWord)
                const searchResult = this.$refs.tree1.getSearchResult()
                this.isEmpty = searchResult.isEmpty
            },
            // 保存音乐信息
            handleClick() {
                console.log(this.musicInfo)
                const params = [{
                    'file_full_path': this.filePath + '/' + this.fileName,
                    ...this.musicInfo
                }]
                this.isLoading = true
                this.$api.Task.updateId3({'music_id3_info': params}).then((res) => {
                    this.isLoading = false
                    if (res.result) {
                        this.$cwMessage('修改成功', 'success')
                    } else {
                        this.$cwMessage('修改失败', 'error')
                    }
                })
            },
            handleBatch() {
                this.$bkInfo({
                    title: '确认要批量修改？',
                    confirmLoading: true,
                    confirmFn: () => {
                        try {
                            this.isLoading = true

                            this.$api.Task.batchUpdateId3({
                                'file_full_path': this.filePath,
                                'select_data': this.checkedData,
                                'music_info': this.musicInfoManual
                            }).then((res) => {
                                this.isLoading = false
                                console.log(res)
                                if (res.result) {
                                    this.$cwMessage('修改成功', 'success')
                                }
                            })
                            return true
                        } catch (e) {
                            console.warn(e)
                            return false
                        }
                    }
                })
            },
            handleBatchAuto() {
                this.$bkInfo({
                    title: '确认要批量修改？',
                    confirmLoading: true,
                    confirmFn: () => {
                        try {
                            this.isLoading = true
                            this.musicInfoManual['select_mode'] = this.selectAutoMode
                            this.musicInfoManual['source_list'] = this.sourceList
                            this.$api.Task.batchAutoUpdateId3({
                                'file_full_path': this.filePath,
                                'select_data': this.checkedData,
                                'music_info': this.musicInfoManual
                            }).then((res) => {
                                this.isLoading = false
                                console.log(res)
                                if (res.result) {
                                    this.$cwMessage('创建成功', 'success')
                                }
                            })
                            return true
                        } catch (e) {
                            console.warn(e)
                            return false
                        }
                    }
                })
            }
        }
    }
</script>
<style lang="postcss">
.bk-table-header .custom-header-cell {
    color: inherit;
    text-decoration: underline;
    text-decoration-style: dashed;
    text-underline-position: under;
}

.music-item {
    cursor: pointer;
}

.music-item:hover {
    color: #1facdd;
}

.label1 {
    width: 80px;
}

.parent {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    grid-template-rows: repeat(1, 1fr);
    grid-column-gap: 0;
    grid-row-gap: 0;
    place-items: center;
}

.title2 {
    font-weight: 500;
}

.song-card {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #E2E2E2;
}

.song-card:hover {
    background: #E2E2E2;
}

.add-button {
    width: 24px;
    height: 24px;
    line-height: 20px;
    display: inline-block;
    background-color: transparent;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-left: 5px;
    font-size: 12px;
    color: rgb(97, 97, 97);
    text-align: center;
    cursor: pointer;
}

.delete-button {
    width: 24px;
    height: 24px;
    line-height: 20px;
    display: inline-block;
    background-color: transparent;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-left: 5px;
    font-size: 12px;
    color: rgb(63, 63, 63);
    text-align: center;
    cursor: pointer;
}

.file-section {
    background: #fff;
    height: calc(100vh - 75px);
    overflow: scroll;
    width: 25%;
    border: 1px solid #173769;
    margin: 10px 0 10px 10px;
    border-radius: 20px;

}

.edit-section {
    background: #fff;
    height: calc(100vh - 75px);
    overflow: scroll;
    border: 1px solid #173769;
    margin: 10px 10px 10px 10px;
    border-radius: 20px;
}

.resource-section {
    background: #fff;
    height: calc(100vh - 75px);
    width: 30%;
    flex: 1;
    overflow: scroll;
    border: 1px solid #173769;
    margin: 10px 10px 10px 0;
    border-radius: 20px;
}

.bk-form-checkbox {
    margin-right: 10px;
}

.success {
    color: #d1cfc5;
}

.failed {
    color: #ac354b;
}

.null {
    color: #333146;
}

button.bk-success {
    background-color: rgb(17, 64, 108) !important;
    border-color: rgb(17, 64, 108) !important;
}

button.bk-primary {
    background-color: rgb(17, 64, 108) !important;
    border-color: rgb(17, 64, 108) !important;
}

button.bk-button-text {
    background-color: transparent !important;
}

.bk-form-checkbox.is-checked .bk-checkbox {
    border-color: rgb(17, 64, 108) !important;
    background-color: rgb(17, 64, 108) !important;
    background-clip: border-box !important;
}

.bk-button-group .bk-button.is-selected {
    border-color: rgb(17, 64, 108) !important;
    color: rgb(17, 64, 108) !important;
}

.bk-button.bk-default:hover {
    border-color: rgb(17, 64, 108) !important;
    color: rgb(17, 64, 108) !important;
}

.bk-form-radio input[type=radio].is-checked {
    color: rgb(17, 64, 108) !important;
}

.bk-steps .bk-step.current .bk-step-icon, .bk-steps .bk-step.current .bk-step-number, .bk-steps .bk-step.current .bk-step-text {
    border-color: rgb(17, 64, 108) !important;
    background-color: rgb(17, 64, 108) !important;
}

.bk-steps .bk-step.done .bk-step-icon, .bk-steps .bk-step.done .bk-step-number, .bk-steps .bk-step.done .bk-step-text {
    border-color: rgb(17, 64, 108) !important;
    color: rgb(17, 64, 108) !important;
}

.bk-icon.icon-arrows-left-circle {
    color: rgb(17, 64, 108) !important;
}

.bk-icon.icon-arrows-right-circle {
    color: rgb(17, 64, 108) !important;
}

.bk-icon.icon-arrows-right-shape {
    color: rgb(17, 64, 108) !important;
}

.bk-icon.icon-arrows-right-shape:hover {
    color: #df4d40 !important;
}

.bk-icon.icon-arrows-left-shape:hover {
    color: #df4d40 !important;
}

.bk-icon.icon-arrows-down-shape:hover {
    color: #df4d40 !important;
}

::-webkit-scrollbar {
    width: 0;
    background-color: transparent;
}

::-webkit-scrollbar-thumb {
    background-color: #f4f5f0;
}
</style>
